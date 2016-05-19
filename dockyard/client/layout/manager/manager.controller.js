(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("managerCtrl", ["sidebarService", managerCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function managerCtrl(sidebarService) {
            var vm  = this;

            sidebarService.hide();

            vm.name = "manager"
        }

})();