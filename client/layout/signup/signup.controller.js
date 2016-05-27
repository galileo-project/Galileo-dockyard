(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("signupCtrl", ["$location", "dataService", "sidebarService", signupCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function signupCtrl($location, dataService, sidebarService) {
            var vm  = this;

            sidebarService.hide();

            vm.signup = signup;


           function signup() {
               if(vm.password1 !== vm.password2){
                   vm.msg = "Password invalid";
               } else {
                   vm.msg = "";

                   dataService.user.signup(vm.name, vm.email, vm.password1).then(function (msg) {
                       if(!msg.err){
                           $location.path("/");
                       }
                   });
               }

           } //sign up end
        } // sign up ctrl end

})();