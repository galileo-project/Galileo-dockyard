'use strict';

var tplData = require('./headData.json');
var json = require('../../../utils/json.js');

module.exports = function (req, res, next, data){
    res.render('head', json.extendJson(tplData, data), function (err, html) {
        if(!err){
            var html = '<!DOCTYPE html>\r\n<html ng-app=\'dockyard\'>' + html + '<body>';
            res.write(html);
        }
    });
}