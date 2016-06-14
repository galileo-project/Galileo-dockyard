(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("homeCtrl", ["dataService", "sidebarService", "$location", homeCtrl])
        .controller("layOutCtrl", ["$scope", "sidebarService", layOutCtrl]);


       /**************************
       *        Controllers      *
       ***************************/
    function homeCtrl(dataService, sidebarService, $location) {
        var vm  = this;

        active();
        vm.name = "home";

        function active() {
            sidebarService.show();
            if(dataService.cookie.get("user") === null){
                $location.path("/login");
            }
        }
    }

    function layOutCtrl($scope, sidebarService) {
        var vm = this;

        active();

        function active() {
            $scope.$on('handleSidebar', handleSidebar);

            function handleSidebar() {
                if(sidebarService.visible) {
                    vm.sidebarClass = "col-sm-3 col-md-2";
                    vm.mainClass    = "col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2"
                } else {
                    vm.sidebarClass = "";
                    vm.mainClass    = "container-fluid";
                }
            }
        } // end of active
} // end of layOutCtrl
})();