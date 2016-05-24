(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("msgBoxCtrl",  ["$scope", "msgService",     msgBoxCtrl])
        .controller("loadingCtrl", ["$scope", "loadingService", loadingCtrl])
        .controller("layOutCtrl",  ["$scope", "$location", "sidebarService", layOutCtrl]);


    /**************************
     *        Controllers      *
     ***************************/
    function msgBoxCtrl($scope, msgService) {
        var vm   = this;
        
        vm.click    = handleClick;
        vm.visible  = false;
        active();

        //functions
        function active() {
            $scope.$on("handleMsg", handleReceive);

            function handleReceive() {
                if(msgService.message !== null) {
                    vm.visible = true;
                    vm.msg = msgService.message;
                    vm.msgType = msgService.msgType;
                }
            }
        } //end of active

        function handleClick() {
            vm.visible = false;
        }
        
    } // end of msgbox ctrl

    function loadingCtrl($scope, loadingService){
        var vm = this;

        vm.visible = false;
        active();

        function active() {
            $scope.$on("handleLoading", handleEvent);

            function handleEvent() {
                vm.visible = loadingService.visible;
            }
        }
    } // end of loading ctrl

    function layOutCtrl($scope, $location, sidebarService) {
        var vm = this;

        active();

        function active() {
            $scope.$on('handleSidebar', handleSidebar);

            function handleSidebar() {
                if(sidebarService.visible) {
                    vm.sidebarURL   = "layout/aside/aside.include.html";
                    vm.sidebarClass = "col-sm-3 col-md-2 ng-scope";
                    vm.mainClass    = "col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2"
                } else {
                    vm.sidebarURL   = "";
                    vm.sidebarClass = "";
                    vm.mainClass    = "container-fluid"

                }
            }
        } // end of active
    } // end of layOutCtrl

})();