(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("githubOauthCtrl", ["$window", "$location", "$routeParams", "dataService", "sidebarService", githubOauthCtrl]);

    /**************************
     *        Controllers      *
     ***************************/
    function githubOauthCtrl($window, $location, $routeParams, dataService, sidebarService) {
        var vm  = this;

        active();
        
        function active() {
            sidebarService.hide();
            var code = getParameterByName("code");
            var state = getParameterByName("state");

            if(code && state){
                dataService.user.github.auth(code, state).then(function(msg){
                    $window.location.href = "/";
                })
            }else{
                dataService.user.github.oauth().then(function (msg) {
                    if(!msg.err){
                        $window.location.href = msg.data
                    }
                })
            }
        }

        function getParameterByName(name, url) {
            if (!url) url = window.location.href;
            name = name.replace(/[\[\]]/g, "\\$&");
            var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
                results = regex.exec(url);
            if (!results) return null;
            if (!results[2]) return '';
            return decodeURIComponent(results[2].replace(/\+/g, " "));
        }

    } // end of github oauth ctrl

})();