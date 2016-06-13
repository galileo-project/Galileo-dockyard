'use strict';

var fs   = require('fs');
var tplData = require('./headData.json');
var json = require('../../../utils/json.js');

module.exports = function (req, res, next, data){
    res.render('head', json.extendJson(tplData, data), function (err, html) {
        if(!err){
            var data = '<!DOCTYPE html>\r\n<html>' + html + '<body>';
            res.write(data);
        }
    });
}