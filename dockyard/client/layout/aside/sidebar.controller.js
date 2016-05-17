(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("sidebarCtrl", sidebarCtrl);


    /**************************
     *        Controllers      *
     ***************************/
    function sidebarCtrl($scope, $location) {
        var vm   = this;

        active();

        //functions
        function active() {
            $scope.$on('$routeChangeSuccess', handleSidebar)

            function handleSidebar() {
                var path = $location.path();
                if(path === '/login' || path === '/signup') {
                    vm.sidebarURL = "";
                } else {
                    vm.sidebarURL = "layout/aside/aside.include.html";
                }
            }
        }
    }

})();