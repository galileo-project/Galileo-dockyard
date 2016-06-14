(function(){
    "use strict";
    angular
        .module("dockyard", ["ngCookies", "dockyard.core",
                             "dockyard.service.ui", "dockyard.service.pagelets", 
                             "dockyard.service.data"]);
})();