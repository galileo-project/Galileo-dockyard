(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("managerCtrl", ["sidebarService", managerCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function managerCtrl(sidebarService) {
            var vm  = this;

           vm.updatePage    = UpdatePage;
           vm.saveSettings  = saveSettings;
           active();

           function UpdatePage(e) {
               var target = e.target.dataset.target;

               if(target === "settings") {
                   onSettings();
               } else if(target === "users") {
                   onUsers();
               }
           } //end of update page

           function saveSettings() {
               dataService.updateSettings(vm.github_client_id, vm.github_client_secret, vm.github_redirect_uri)
                          .then(function (msg) {});
           } //end of saveSettings

           function active() {
               vm.subPage = "layout/manager/manager.settings.include.html";
               sidebarService.hide();
               onSettings();
           } //end of active

           function onSettings() {
               vm.subPage = "layout/manager/manager.settings.include.html";
               //load settings data
               dataService.getSettings().then(function (msg) {
                   if(!msg.err) {
                       vm.github_client_id      = msg.data.github_client_id;
                       vm.github_client_secret  = msg.data.github_client_secret;
                       vm.github_redirect_uri   = msg.data.github_redirect_uri;
                   }
               });
           } // end of settings

           function onUsers() {
               vm.subPage = "layout/manager/manager.users.include.html";
           } // end of users

        } //end of managerCtrl

})();