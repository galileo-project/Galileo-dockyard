'use strict';

var pagewapper = require('../../../utils/pagelet.js');

module.exports = function (req, res, next, data){
    res.render('menu', data, function (err, html) {
        if(!err){
            res.write(pagewapper.wrapper('menu', html));
        }
    });
}