(function(){
    "use strict"
    angular
        .module("dockyard.core")
        .controller("homeCtrl", ["sidebarFct", homeCtrl]);


       /**************************
       *        Controllers      *
       ***************************/
        function homeCtrl(sidebarFct) {
            sidebarFct.show();
            var vm  = this;

            vm.name = "home";


        }

})();