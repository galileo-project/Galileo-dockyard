(function(){
    "use strict";
    //dockyard API URL
    var HOST         = "http://localhost:8080";
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
        .factory("dataService",      dataService);


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

        // msg handle
        function apiHandleError(msg) {
            var err, code;
            loadingService.hide();

            if(msg.status === -1) {
                err  = "Unknown error";
                code = 1;
            } else {
                err  = msg.error;
                code = msg.code;
            }

            if(code < 2000){
                msgService.error(err);
            } else {
                msgService.warn(err);
            }

            return wrapperMsg(true, err);
        }

        function apiHandleSuccess(msg) {
            loadingService.hide();
            if(msg.code !== 0){
                return apiHandleError(msg);
            } else {
                return wrapperMsg(false, msg.msg);
            }
        }

        function wrapperMsg(err, msg) {
            return {
                err: err,
                msg: msg
            };
        }
    }
})();