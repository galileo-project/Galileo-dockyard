'use strict';

var BigPipe = require('../../utils/bigpipe.js');
var pagelets = require('../../pagelets/index.js');

function homeHandler(req, res, next) {
    var bp = new BigPipe(req, res, next);
    bp.push(pagelets.head);
    bp.push(pagelets.manager.layout.login);
    bp.push(pagelets.navbar);
    bp.finish(); 
}

module.exports = {
    home: homeHandler
}