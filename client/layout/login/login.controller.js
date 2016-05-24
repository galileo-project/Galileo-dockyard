(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("loginCtrl", ["$location", "sidebarService", "dataService", loginCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function loginCtrl($location, sidebarService, dataService) {
            var vm  = this;

            sidebarService.hide();

            vm.login = login;

            function login() {
                var data = {name:     vm.name,
                            password: vm.password};

                dataService.userLogin().then(function(msg) {
                    if(!msg.err) {
                        $location.path("/");
                    }
                });
            } // end of login
        } // end of login ctrl

})();