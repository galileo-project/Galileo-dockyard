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

})();