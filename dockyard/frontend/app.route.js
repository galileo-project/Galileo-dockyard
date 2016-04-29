(function(){
    "use strict";
    angular
        .module("dockyard.route", ["ngRoute"])
        .config(route);

    /************************
    *       routes          *
    *************************/
    function route($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl:    "sections/home/home.tpl.html",
                controller:     "homeCtrl",
                controllerAs :  "home"
            })
            .when("/login", {
                templateUrl:    "sections/login/login.tpl.html",
                controller:     "loginCtrl",
                controllerAs :  "login"
            })
            .otherwise("/");
    }

})()