'use strict';

var head        = require('./modules/head/index.js');
var menu        = require('./modules/menu/index.js');
var layoutHome  = require('./modules/layout/home.js');

var layout = {
    home: layoutHome
};

module.exports = {
    head:   head,
    menu:   menu,
    layout: layout
}