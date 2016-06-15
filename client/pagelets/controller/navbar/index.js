'use strict';

var pagelet = require('../../../utils/pagelet.js');
var tplData = require('./navbarData.json');
var json = require('../../../utils/json.js');


module.exports = function (req, res, next, data){
    res.render('navbar', json.extendJson(tplData, data), function (err, html) {
        if(!err){
            res.write(pagelet.wrapper('navbar', html));
        }
    });
}