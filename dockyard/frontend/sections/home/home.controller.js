(function(){
    "use strict"
    angular
        .module("dockyard.core")
        .controller("homeCtrl", homeCtrl);


       /**************************
       *        Controllers      *
       ***************************/
        function homeCtrl() {
            var vm  = this;

            vm.name = "hello"
        }

})()