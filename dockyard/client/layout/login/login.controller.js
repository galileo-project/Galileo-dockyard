(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("loginCtrl", loginCtrl);

       /**************************
       *        Controllers      *
       ***************************/
        function loginCtrl() {
            var vm  = this;

            vm.name = "login"
        }

})();