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

            active();

            vm.name = "home";

            function active() {
                sidebarService.hide();

                dataService.getUser().then(function (msg) {
                    vm.test = msg;
                });

            }
        }

})();