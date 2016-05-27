(function(){
    "use strict";
    angular
        .module("dockyard.factory.data", [])
        .factory("dataService", dataService);

    function dataService(apiService) {
        var cache = new CacheDriver();
        var user    = {
            auth:           userAuth,
            signup:         userSignup
        };
        var sys     = {
            get_settings:   sysgetSettings,
            get_sys_logs:   sysGetSysLogs,
            save_settings:  sysSaveSettings
        };
        var app     = {

        };
        var manager = {
            auth:           managerAuth,
            all:            userAll,
            del_user_by_id: userDelById
        };

        var result =  {
            cache:      cache,
            sys:        sys,
            user:       user,
            app:        app,
            manager:    manager
        };

        /*-------------data functions--------------*/
        function userAuth(name, password) {
            return "auth";
        }
        function userDelById(uid) {
            return apiService.managerUserDelete(uid);
        }
        function userAll() {
            return apiService.managerUsers();
        }
        function userSignup(name, email, password) {
            return apiService.userSignUp(name, email, password);
        }
        function sysgetSettings() {
            return apiService.getSettings();
        }
        function sysSaveSettings(github_client_id, github_client_secret, github_redirect_uri) {
            return apiService.updateSettings(github_client_id, github_client_secret, github_redirect_uri);
        }
        function sysGetSysLogs() {
            return apiService.managerSysLogs();
        }
        function managerAuth(name, password) {
            return apiService.managerLogin(name, password);
        }
        /*-----------CacheDriver------------*/
        function CacheDriver() {
            this.__data = {};
        }

        CacheDriver.prototype.set = function (key, value) {
            this.__data[key] = value;
        };

        CacheDriver.prototype.get = function (key) {
            return this.__data[key];
        };

        return result;
    }

})();