(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("githubOauthCtrl", ["$location", "dataService", "sidebarService", githubOauthCtrl]);

    /**************************
     *        Controllers      *
     ***************************/
    function githubOauthCtrl($location, dataService, sidebarService) {
        var vm  = this;

        sidebarService.hide();

        active();
        
        function active() {
            dataService.githubOauth().then(function (msg) {
                //TODO github oauth
            })
        }

    } // github oauth ctrl end

})();