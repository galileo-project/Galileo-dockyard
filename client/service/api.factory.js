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
    var HOST                = window.location.origin;
    var API                 = HOST + "/api";
    var PUBLIC              = API + "/public";

    var USER                = API  + "/user";
    var USER_LOGIN          = HOST + "/auth/login";
    var USER_SIGNUP         = USER;
    var USER_CH_PWD         = USER;
    var USER_DELETE         = USER;

    var APP                 = API + "/app";
    var GET_APPS            = APP + "/list";
    var GET_APP             = APP;

    var GITHUB              = PUBLIC + "/github";

    var MANAGER             = API + "/manager";
    var SETTINGS            = MANAGER + "/settings";
    var MANAGER_AUTH        = MANAGER + "/auth/login";
    var MANAGER_USERS       = MANAGER + "/user";
    var MANAGER_DEL_USER    = MANAGER + "/user";

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
            
            getSettings:    getSettings,
            updateSettings: updateSettings,
            managerLogin:   managerLogin,
            managerUsers:   managerUsers,
            
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
        
        function getSettings() {
            return apiGet(SETTINGS);
        }
        
        function updateSettings(github_client_id, github_client_secret, github_redirect_uri) {
            var data = {github_client_id:       github_client_id,
                        github_client_secret:   github_client_secret,
                        github_redirect_uri:    github_redirect_uri};
            return apiPost(SETTINGS, data);
        }
        
        function managerLogin(name, password) {
            var data = {manager_name:       name,
                        manager_pwd:        password};
            
            return apiPost(MANAGER_AUTH, data)
        }

        function managerUsers() {
            return apiGet(MANAGER_USERS)
        }

        function managerDelUser(uid) {
            var data = {uid: uid};

            return apiDelete()
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

        function _wrapperMsg(err, data) {
            return {
                err:  err,
                data: data
            };
        }
    }
})();