(function(){
    "use strict";
    angular
        .module("dockyard.factory.data", [])
        .factory("dataService", dataService);

    function dataService() {
        return {
            cache:      cache,
            sys:        sys,
            user:       user,
            app:        app,
            manager:    manager
        };
    }

    var cache = new CacheDriver();
    var user    = {
        auth:           userAuth,
        del_by_id:      userDelById,
        all:            userAll
    };
    var sys     = {};
    var app     = {};
    var manager = {};
    /*-------------data functions--------------*/
    function userAuth(name, password) {
        return "auth";
    }
    function userDelById(id) {
        return "del by id";
    }
    function userAll() {
        return [];
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

})();