/**
 * Created by tor on 2016/4/30.
 */
(function(){
    "use strict";
    angular
        .module("dockyard.factory.ui", [])
        .factory("msgService",      ["$rootScope", msgService])
        .factory("loadingService",  ["$rootScope", loadingService])
        .factory("sidebarService",  ["$rootScope", sidebarService]);


    /**********************
     *       functions     *
     ***********************/
    function msgService($rootScope) {
        var msgService = {};

        msgService.message    = "";
        msgService.msgType    = "";

        msgService.error    = handleError;
        msgService.warn     = handleWarn;
        msgService.success  = handleSuccess;
        msgService.info     = handleInfo;

        return msgService;

        function handleError(msg) {
            msgService.message = msg;
            msgService.msgType = "msgError";
            sendMsg();
        }


        function handleWarn(msg) {
            msgService.message = msg;
            msgService.msgType = "msgWarn";
            sendMsg();
        }


        function handleSuccess(msg) {
            msgService.message = msg;
            msgService.msgType = "msgSuccess";
            sendMsg();
        }


        function handleInfo(msg) {
            msgService.message = msg;
            msgService.msgType = "msgInfo";
            sendMsg();
        }

        function sendMsg() {
            $rootScope.$broadcast("handleMsg");
        }
    } //end of msgService

    function loadingService($rootScope) {
        var loadingService = {};

        loadingService.visible  = false;
        loadingService.show     = show;
        loadingService.hide     = hide;

        return loadingService;

        function show() {
            loadingService.visible = true;
            sendEvent();
        }

        function hide() {
            loadingService.visible = false;
            sendEvent();
        }
        
        function sendEvent() {
            $rootScope.$broadcast("handleLoading")
        }
    }  //end of loadingService

    function sidebarService($rootScope) {
        var sidebarService = {};

        sidebarService.visible  = true;
        sidebarService.show     = show;
        sidebarService.hide     = hide;

        return sidebarService;

        function show() {
            sidebarService.visible = true;
            sendEvent();
        }

        function hide() {
            sidebarService.visible = false;
            sendEvent();
        }

        function sendEvent() {
            $rootScope.$broadcast("handleSidebar");
        }
    }  //end of sidebarService
})();