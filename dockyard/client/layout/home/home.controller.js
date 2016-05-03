(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("homeCtrl", ["getUserService", homeCtrl]);


       /**************************
       *        Controllers      *
       ***************************/
        function homeCtrl(getUserService) {
            var vm  = this;

            vm.name = "home";
            getUserService.getData();

        }

})();