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
               var data = {user_name:  vm.name,
                           user_email: vm.email,
                           user_pwd:   vm.password1};

               if(vm.password1 !== vm.password2){
                   vm.msg = "Password invalid";
               } else {
                   vm.msg = "";

                   dataService.userSignUp(data).then(function (msg) {
                       if(!msg.err){
                           $location.path("/");
                       }
                   });
               }

           } //sign up end
        } // sign up ctrl end

})();