/**
 * Created by tor on 2016/4/30.
 */
(function(){
    "use strict";
    angular
        .module("dockyard.factory.ui", [])
        .factory("sidebarFct", sidebarFct);


    /**********************
     *       functions     *
     ***********************/
    function sidebarFct() {
        //var sideBar = angular.element("aside");

        return {
            hide: hide,
            show: show
        };

        function hide() {
            //sideBar.$addClass("hide");
        }

        function show() {
            //sideBar.$removeClass("hide");
        }

    }
})()