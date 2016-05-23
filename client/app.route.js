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
                templateUrl:    "layout/home/home.tpl.html",
                controller:     "homeCtrl",
                controllerAs :  "home"
            })
            .when("/login", {
                templateUrl:    "layout/login/login.tpl.html",
                controller:     "loginCtrl",
                controllerAs :  "login"
            })
            .when("/signup", {
                templateUrl:    "layout/signup/signup.tpl.html",
                controller:     "signupCtrl",
                controllerAs :  "signup"
            })
            .when("/oauth/github", {
                templateUrl:    "layout/oauth/github.tpl.html",
                controller:     "githubOauthCtrl",
                controllerAs :  "githubOauth"
            })
            .when("/manager", {
                templateUrl:    "layout/manager/manager.tpl.html",
                controller:     "managerCtrl",
                controllerAs :  "manager"
            })
            .otherwise("/");
    }

})();