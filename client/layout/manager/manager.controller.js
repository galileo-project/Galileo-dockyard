(function(){
    "use strict";
    angular
        .module("dockyard.core")
        .controller("managerCtrl", ["dataService", "sidebarService", "$cookies", managerCtrl]);

       /**************************
       *        Controllers      *
       ***************************/
        function managerCtrl(dataService, sidebarService, $cookies) {
            var vm  = this;

           vm.updatePage    = UpdatePage;
           vm.saveSettings  = saveSettings;
           vm.login         = login;
           //active();

           dataService.cache.set("test", "TEST");
           console.log(dataService.user.auth("a", "b"));
           console.log(dataService.cache.get("test"));

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

               onUsers();
               // if($cookies.get("manager")){
               //     onLogin();
               // } else {
               //     onUsers();
               // }

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
               dataService.managerUsers().then(function (msg) {
                   if(!msg.err) {
                       vm.users = msg.data;
                   }
               });
           } // end of users

        } //end of managerCtrl

})();