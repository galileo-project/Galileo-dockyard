(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("githubOauthCtrl", ["$location", "dataService", githubOauthCtrl]);

    /**************************
     *        Controllers      *
     ***************************/
    function githubOauthCtrl($location, dataService) {
        var vm  = this;

        activate();
        
        function activate() {
            dataService.githubOauth().then(function (msg) {
                //TODO github oauth
            })
        }

    } // github oauth ctrl end

})();