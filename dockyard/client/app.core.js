(function(){
    "use strict";
    angular
        .module("dockyard.core", [])
        .controller("appCtrl", appCtrl);

    function appCtrl(){
        var vm = this;

        vm.path = true;
    }
})();