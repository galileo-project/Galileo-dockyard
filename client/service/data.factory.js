(function(){
    "use strict";
    angular
        .module("dockyard.factory.data", [])
        .factory("dataService", dataService);

    function dataService(apiService, $interval, $cookies) {
        var CACHE = new Cacher();
        var user    = {
            auth:           userAuth,   //login in
            signup:         userSignup,
            loginout:       userLogout,
            exists:         userExists,
            info:           userInfo,
            id:             userCurrId,
            apps:           userApps
        };
        var sys     = {
            get_settings:   sysgetSettings,
            get_sys_logs:   sysGetSysLogs,
            save_settings:  sysSaveSettings
        };
        var app     = {
            exists:         appExists,
            builds:         appBuilds,
            id:             appCurrId
        };
        var build   = {
            eixsts:         buildExists,
            id:             buildCurrId
        };
        var manager = {
            auth:           managerAuth,
            all:            managerGetUserAll,
            exists:         managerExists,
            logout:         managerLogout,
            del_user_by_id: managerDelUserById
        };
        var cookie  = {
            get:            getCookie,
            set:            setCookie
        };

        var result =  {
            cache:      CACHE,
            sys:        sys,
            user:       user,
            app:        app,
            manager:    manager,
            build:      build,
            cookie:     cookie
        };

        /*-------------data functions--------------*/
        //user api
        function userAuth(name, password) {
            return "auth";
        }
        function userSignup(name, email, password) {
            return apiService.userSignUp(name, email, password);
        }
        function userInfo() {
            var key = "userInfo";
            return cacheWrapper(apiService.getUser, key);
        }
        function userLogout() {

        }
        function userExists() {

        }
        function userCurrId() {

        }
        function userApps() {

        }

        //app api
        function appExists() {

        }
        function appBuilds() {

        }
        function appCurrId() {

        }

        //build api
        function buildExists() {

        }
        function buildCurrId() {

        }

        //system api
        function sysgetSettings() {
            return apiService.getSettings();
        }
        function sysSaveSettings(github_client_id, github_client_secret, github_redirect_uri) {
            return apiService.updateSettings(github_client_id, github_client_secret, github_redirect_uri);
        }
        function sysGetSysLogs() {
            return apiService.managerSysLogs();
        }

        ////manager api
        function managerAuth(name, password) {
            return apiService.managerLogin(name, password);
        }
        function managerExists() {

        }
        function managerLogout() {

        }
        function managerDelUserById(uid) {
            return apiService.managerUserDelete(uid);
        }
        function managerGetUserAll() {
            return apiService.managerUsers();
        }

        //cookie handle
        function getCookie(key) {
            var result = $cookies.get(key);
            if(typeof result === "undefined"){
                result = null;
            }
            return result;
        }
        function setCookie(key, value) {

        }
        /*-----------Cacher------------*/
        function Cacher() {
            this.__defaultExpire    = 120;      //second
            this.__capacity         = 200;      //capacity of Cacher
            this.__length           = 0;
            this.__currData         = null;
            this.__data             = {};
        }
        Cacher.prototype.set = function (key, value, expire) {
            if(this.__length >= this.__capacity){
                return;
            }
            expire = typeof expire === "undefined" ? this.__defaultExpire: expire;
            this.__data[key] = {
                value:  value,
                expire: expire + timestamp(),
                hits:   0
            };
            this.__length += 1;
        };
        Cacher.prototype.get = function (key) {
            var result = this.__data[key];
            if(typeof result === "undefined"){
                this.__currData = null;
            } else {
                this.__currData = result.value;
            }
            return this.__currData;
        };
        Cacher.prototype.then = function (fn) {
            return fn(this.__currData);
        };
        Cacher.prototype.__routine__ = function () {
            this.__handleExpire__();
        };
        Cacher.prototype.__handleExpire__ = function () {
            for(var key in this.__data){
                if(this.__data.hasOwnProperty(key)){
                    if(this.__data[key].expire <= timestamp()){
                        delete this.__data[key];
                    }
                }
            }
        };

        
        function interCall(){
            CACHE.__routine__();
        }
        $interval(interCall, 2000);
        
        /*----------utils---------*/
        function timestamp() {
            return Math.floor(Date.now() / 1000);
        }
        
        function cacheWrapper(fn, key, data) {
            if(CACHE.get(key) === null){
                return fn(data).then(function (msg) {
                    if(!msg.err){
                        CACHE.set(key, msg);
                    }
                    return msg;
                });
            } else {
                return CACHE;
            }
        }

        return result;
    }

})();