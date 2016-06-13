'use strict';

var head        = require('./controller/head/index.js');
var menu        = require('./controller/menu/index.js');
var layoutHome  = require('./controller/layout/home.js');

var layout = {
    home: layoutHome
};

module.exports = {
    head:   head,
    menu:   menu,
    layout: layout
}