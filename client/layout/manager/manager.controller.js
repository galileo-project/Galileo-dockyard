(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("managerCtrl", ["sidebarService", "dataService", managerCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function managerCtrl(sidebarService, dataService) {
            var vm  = this;

           vm.updatePage    = UpdatePage;
           vm.saveSettings  = saveSettings;
           vm.login         = login;
           active();

           function login() {
               dataService.managerLogin(vm.name, vm.password)
                   .then(function (msg) {
                       if(!msg.err) {
                           onUsers();
                       }
                   })
           }

           function UpdatePage(e) {
               var target = e.target.dataset.target;

               if(target === "settings") {
                   onSettings();
                   console.log("update page");
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
               console.log("active");
               onLogin();
           } //end of active

           /***********handler include page**************/
           function onLogin() {
               vm.subPage            = "layout/manager/manager.login.include.html";
               vm.managerSideVisible = false;
           } // end of manager login

           function onSettings() {
               vm.subPage = "layout/manager/manager.settings.include.html";
               vm.managerSideVisible = true;
               //load settings data
               dataService.getSettings().then(function (msg) {
                   if(!msg.err && msg.data !== null) {
                       vm.github_client_id      = msg.data.github_client_id;
                       vm.github_client_secret  = msg.data.github_client_secret;
                       vm.github_redirect_uri   = msg.data.github_redirect_uri;
                   }
               });
           } // end of settings

           function onUsers() {
               vm.subPage            = "layout/manager/manager.users.include.html";
               vm.managerSideVisible = true;
           } // end of users

        } //end of managerCtrl

})();