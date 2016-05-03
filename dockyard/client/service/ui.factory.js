/**
 * Created by tor on 2016/4/30.
 */
(function(){
    "use strict";
    angular
        .module("dockyard.factory.ui", [])
        .factory("msgFct", ["$rootScope", msgFct]);


    /**********************
     *       functions     *
     ***********************/
    function msgFct($rootScope) {
        var msgService = {};

        msgService.message    = "";
        msgService.msgType    = "";

        msgService.error    = handleError;
        msgService.warn     = handleWarn;
        msgService.success  = handleSuccess;
        msgService.info     = handleInfo;


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

        return msgService
    }
})();