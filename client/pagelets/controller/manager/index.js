'use strict';

var login = require('./layout/login.js')
var home = require('./layout/home.js')

var layout = {
    login:  login,
    home:   home
}

module.exports = {
    layout: layout
}