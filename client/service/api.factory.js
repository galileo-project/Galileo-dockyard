(function(){
    "use strict";
    //dockyard API URL
    var HOST         = "http://203.88.167.78:8080";
    var API          = HOST + "/api";
    var USER         = API  + "/user";

    var USER_LOGIN   = HOST + "/auth/login";
    var USER_SIGNUP  = USER;
    var USER_CH_PWD  = USER;
    var USER_DELETE  = USER;
    var GET_USER     = USER;

    var APP          = API + "/app";
    var GET_APPS     = APP + "/list";
    var GET_APP      = APP;

    angular
        .module("dockyard.factory.api", [])
        .factory("dataService",         dataService);


    /**********************
    *       functions     *
    ***********************/
    function dataService($http, msgService, loadingService, $httpParamSerializerJQLike) {
        return {
            userLogin:      userLogin,
            userSignUp:     userSignUp,
            userChPwd:      userChPwd,
            userDelete:     userDelete,
            getUser:        getUser,
            getApps:        getApps,
            getApp:         getApp,
            githubOauth:    githubOauth
        };


        /***************************
         *      api functions      *
         ***************************/


        function userLogin(data) {
            return apiPost(USER_LOGIN, data);
        }

        function userSignUp(data) {
            return apiPost(USER_SIGNUP, data);
        }

        function userChPwd() {

        }

        function userDelete() {

        }

        function getUser() {
            return apiGet(GET_USER);
        }

        function getApps() {

        }

        function getApp() {

        }
        
        function githubOauth() {
            return apiGet()
        }

        /**************************
         *       Common function   *
         * *************************/

        //api functions
        function apiGet(url) {
            loadingService.show();

            var ret = $http.get(url).then(function (response) {
                return response.data;
            }, function (response) {
                return response;
            });

            return ret.then(apiHandleSuccess, apiHandleError)
        }

        function apiPost(url, data) {
            loadingService.show();

            var ret = $http({
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                method:  'POST',
                url:     url,
                data:    $httpParamSerializerJQLike(data)
            }).then(function (response) {
                return response.data;
            }, function (response) {
                return response;
            });

            return ret.then(apiHandleSuccess, apiHandleError);
        }

        // handle api error
        function apiHandleError(msg) {
            loadingService.hide();

            return _wrapperMsg(true, info);
        }

        // handle api success
        function apiHandleSuccess(msg) {
            loadingService.hide();

            if(msg.code !== 0){
                return apiHandleError(msg);
            } else {
                return _wrapperMsg(false, msg.data);
            }
        }

        function _handleMsg(msg) {
            var info, code;

            if(msg.status === -1) {
                info = "Unknown error";
                code = 1;
            } else {
                info = msg.info;
                code = msg.code;
            }

            if(code < 30000){
                msgService.error(info);
            } else if(code < 80000) {
                msgService.warn(info);
            } else {
                msgService.info(info);
            }
        }

        function _wrapperMsg(err, msg) {
            return {
                err: err,
                msg: msg
            };
        }
    }
})();