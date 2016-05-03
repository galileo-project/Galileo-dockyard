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
        .factory("getUserService",      getUserService)
        .factory("signUpService",       signUpService)
        .factory("chPwdService",        chPwdService)
        .factory("delUserService",      delUserService)
        .factory("getAppService",       getAppService)
        .factory("getAppsService",      getAppsService);


    /**********************
    *       functions     *
    ***********************/
    function getUserService($http, msgFct) {
        return {getData: getData};

        function getData() {
            var ret = $http.get(GET_USER).then(apiHandleSuccess, apiHandleError);
            console.log(ret.$$state);
            console.log(ret.$$state.value);
            return unwrapperMsg(ret);
        }
    }

    function signUpService() {
        return apiPost(USER_SIGNUP);
    }

    function chPwdService() {

    }

    function delUserService() {

    }

    function getAppService() {

    }

    function getAppsService() {

    }


    /**************************
    *       Common function   *
    * *************************/

    function apiHandleError(msg) {
        return wrapperMsg(true, "error");
    }

    function apiHandleSuccess(msg) {
        if(msg.code !== 0){
            return apiHandleError(msg.error);
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

    function unwrapperMsg(msg, msgFct) {
        if(msg.err == true){
            msgFct.error(msg.msg);
            return false;
        } else {
            return msg.msg;
        }
    }


})();