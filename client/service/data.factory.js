(function(){
    "use strict";
    angular
        .module("dockyard.factory.data", [])
        .factory("dataService", dataService);

    function dataService(apiService) {
        var cache = new CacheDriver();
        var user    = {
            auth:           userAuth,
            all:            userAll
        };
        var sys     = {
            get_settings:   SysgetSettings,
            save_settings:  SysSaveSettings
        };
        var app     = {};
        var manager = {
            auth:           managerAuth,
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
            return apiService.userDelete(uid);
        }
        function userAll() {
            return apiService.managerUsers();
        }
        function SysgetSettings() {
            return apiService.getSettings();
        }
        function SysSaveSettings(github_client_id, github_client_secret, github_redirect_uri) {
            return apiService.updateSettings(github_client_id, github_client_secret, github_redirect_uri);
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