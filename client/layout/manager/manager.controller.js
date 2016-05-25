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

           vm.updatePage = UpdatePage;
           active();

           function UpdatePage(e) {
               var target = e.target.dataset.target;

               if(target === "settings") {
                   vm.subPage = "layout/manager/manager.settings.include.html";
               } else if(target === "users") {
                   vm.subPage = "layout/manager/manager.users.include.html";
               }
           } //end of update page

           function active() {
               vm.subPage = "layout/manager/manager.settings.include.html";
               sidebarService.hide();
           } //end of active
        } //end of managerCtrl

})();