(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("homeCtrl", ["dataService", "sidebarService", "$location", homeCtrl]);


       /**************************
       *        Controllers      *
       ***************************/
        function homeCtrl(dataService, sidebarService, $location) {
            var vm  = this;

            active();
            vm.name = "home";

            function active() {
                console.log("active");
                sidebarService.show();
                if(dataService.cookie.get("user") === null){
                    $location.path("#/login");
                }

                dataService.user.info().then(function (msg) {
                    console.log("msg> ");
                    console.log(msg);
                    vm.test= msg.data;
                });
            }
        }

})();