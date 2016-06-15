'use strict';

var BigPipe = require('../../utils/bigpipe.js');
var pagelets = require('../../pagelets/index.js');

function notfoundHandler(req, res, next) {
    var bp = new BigPipe(req, res, next, 404);
    bp.push(pagelets.head);
    bp.push(pagelets.error.notfound);
    bp.push(pagelets.navbar);
    bp.finish(); 
}

module.exports = {
    notfound: notfoundHandler
}