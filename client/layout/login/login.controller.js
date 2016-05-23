(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("loginCtrl", ["sidebarService", loginCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function loginCtrl(sidebarService) {
            var vm  = this;

            sidebarService.hide();

            vm.name = "login";
        }

})();