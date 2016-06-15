'use strict';

var BigPipe = require('../../utils/bigpipe.js');
var pagelets = require('../../pagelets/index.js');

function loginHandler(req, res, next) {
    var bp = new BigPipe(req, res, next);
    bp.push(pagelets.layout.login);
    bp.finish(); 
}

module.exports = {
    login: loginHandler
}