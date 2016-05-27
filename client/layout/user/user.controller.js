(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("userCtrl", ["dataService", "sidebarService", userCtrl]);

    /**************************
     *        Controllers      *
     ***************************/
    function userCtrl(dataService, sidebarService) {
        var vm  = this;
        sidebarService.show();

    } // user ctrl end

})();