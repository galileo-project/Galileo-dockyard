'use strict';

var BigPipe = require('../../../utils/bigpipe.js');
var pagelets = require('../../../pagelets/index.js');

module.exports = function (req, res, next) {
    var bp = new BigPipe(req, res, next);
    bp.push(pagelets.head);
    bp.push(pagelets.manager.layout.home);
    bp.push(pagelets.navbar);
    bp.finish(); 
}
