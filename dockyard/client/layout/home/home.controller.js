(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("homeCtrl", ["dataService", "sidebarService", homeCtrl]);


       /**************************
       *        Controllers      *
       ***************************/
        function homeCtrl(dataService, sidebarService) {
            var vm  = this;

            sidebarService.hide();
            active();

            vm.name = "home";

            function active() {
                dataService.getUser().then(function (msg) {
                    vm.test = msg;
                });

            }
        }

})();