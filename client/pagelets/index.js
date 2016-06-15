'use strict';

var head        = require('./controller/head/index.js');
var navbar      = require('./controller/navbar/index.js');
var sidebar     = require('./controller/sidebar/index.js');
var layoutHome  = require('./controller/layout/home.js');
var manager     = require('./controller/manager/index.js')

var layout = {
    home: layoutHome
};

module.exports = {
    head:       head,
    navbar:     navbar,
    sidebar:    sidebar,
    layout:     layout,
    manager:    manager
}