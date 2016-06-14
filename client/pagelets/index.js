'use strict';

var head        = require('./controller/head/index.js');
var menu        = require('./controller/menu/index.js');
var sidebar        = require('./controller/sidebar/index.js');
var layoutHome  = require('./controller/layout/home.js');

var layout = {
    home: layoutHome
};

module.exports = {
    head:       head,
    menu:       menu,
    sidebar:    sidebar,
    layout:     layout
}