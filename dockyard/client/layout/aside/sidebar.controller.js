(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("sidebarCtrl", ["$scope", "$location", "sidebarService", sidebarCtrl]);


    /**************************
     *        Controllers      *
     ***************************/
    function sidebarCtrl($scope, $location, sidebarService) {
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