(function(){
    "use strict";
    angular
        .module("dockyard.route", ["ngRoute"])
        .config(routes);

    /************************
    *       routes          *
    *************************/
    function routes($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl: '../../html/tpl/home.tpl.html',
                controller: 'HomeController as home'
            })

    }

})()