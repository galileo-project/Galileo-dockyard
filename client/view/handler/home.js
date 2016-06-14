'use strict';

var BigPipe = require('../../utils/bigpipe.js');
var pagelets = require('../../pagelets/index.js');

function homeHandler(req, res, next) {
    var bp = new BigPipe(req, res, next);
    bp.push(pagelets.head);
    bp.push(pagelets.layout.home);
    bp.push(pagelets.menu);   
    bp.finish(); 
}

module.exports = {
    home: homeHandler
}