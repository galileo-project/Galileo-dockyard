(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("sidebarCtrl", ["$scope", "sidebarService", sidebarCtrl]);


    /**************************
     *        Controllers      *
     ***************************/
    function sidebarCtrl($scope, sidebarService, $location) {
        var vm = this;

        active();

        //functions
        function active() {
            $scope.$on('handleSidebar', handleSidebar)

            function handleSidebar() {
                if(sidebarService.visible) {
                    vm.sidebarURL = "layout/aside/aside.include.html";
                } else {
                    vm.sidebarURL = "";
                }
            }
        } //end of active
    }

})();