(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("msgBoxCtrl",  ["$scope", "msgService",     msgBoxCtrl])
        .controller("loadingCtrl", ["$scope", "loadingService", loadingCtrl]);


    /**************************
     *        Controllers      *
     ***************************/
    function msgBoxCtrl($scope, msgService) {
        var vm   = this;
        
        vm.click = handleClick;
        vm.visible = false;
        active();

        //functions
        function active() {
            $scope.$on("handleMsg", handleReceive);

            function handleReceive() {
                vm.visible = true;
                vm.msg     = msgService.message;
                vm.msgType = msgService.msgType;
            }
        }

        function handleClick() {
            vm.visible = false;
        }
        
    }

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
    }

})();