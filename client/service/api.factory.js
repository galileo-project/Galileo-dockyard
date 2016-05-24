(function(){
    "use strict";
    // API status code
    var CODE_API_SUCCESS   = 0;        // code equal to 0
    var CODE_SUCCESS       = 10000;    // less than 10000
    var CODE_UNKNOWN_ERROR = 10001;    // code equal to 10001
    var CODE_ERROR         = 30000;    // less than 30000 and greater than 10000
    var CODE_WARN          = 80000;    // less than 80000 and greater than 30000
    var CODE_INFO          = 99999;    // less than 99999 and greater than 80000

    //dockyard API URL
    var HOST         = "http://203.88.167.78:8080";
    var API          = HOST + "/api";
    var PUBLIC       = API + "/public";

    var USER         = API  + "/user";
    var USER_LOGIN   = HOST + "/auth/login";
    var USER_SIGNUP  = USER;
    var USER_CH_PWD  = USER;
    var USER_DELETE  = USER;

    var APP          = API + "/app";
    var GET_APPS     = APP + "/list";
    var GET_APP      = APP;

    var GITHUB       = PUBLIC + "/github";

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
            return apiGet(USER);
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
            _handleMsg(msg);
            return _wrapperMsg(true, msg.info);
        }

        // handle api success
        function apiHandleSuccess(msg) {
            // TODO debug
            console.log(msg);
            loadingService.hide();

            if(msg.code >= CODE_SUCCESS){
                return apiHandleError(msg);
            } else {
                _handleMsg(msg);
                return _wrapperMsg(false, msg.data);
            }
        }

        function _handleMsg(msg) {
            var info, code;

            if(msg.status === -1) {
                info = "Unknown error";
                code = CODE_UNKNOWN_ERROR;
            } else {
                info = msg.info;
                code = msg.code;
            }

            if(code < CODE_SUCCESS){
                msgService.success(info);
            } else if(code < CODE_ERROR){
                msgService.error(info);
            } else if(code <= CODE_WARN) {
                msgService.warn(info);
            } else if(code <= CODE_INFO){
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