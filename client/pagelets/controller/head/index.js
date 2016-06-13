'use strict';

var fs = require('fs');

module.exports = function (req, res, next, data){
    res.render('head', data, function (err, html) {
        if(!err){
            var data = '<!DOCTYPE html>\r\n<html>' + html + '<body>';
            res.write(data);
        }
    });
}