(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("githubOauthCtrl", ["$window", "dataService", "sidebarService", githubOauthCtrl]);

    /**************************
     *        Controllers      *
     ***************************/
    function githubOauthCtrl($window, dataService, sidebarService) {
        var vm  = this;

        active();
        
        function active() {
            sidebarService.hide();
            dataService.user.oauth().then(function (msg) {
                if(!msg.err){
                    $window.location.href = msg.data
                }
            })
        }

    } // end of github oauth ctrl

})();