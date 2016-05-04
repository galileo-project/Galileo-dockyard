(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("homeCtrl", ["dataService", homeCtrl]);


       /**************************
       *        Controllers      *
       ***************************/
        function homeCtrl(dataService) {
            var vm  = this;

            vm.name = "home";
            dataService.getUser().then(function (msg) {
                vm.test = msg;
            });

        }

})();