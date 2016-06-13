'use strict';

var pagelet = require('../../../utils/pagelet.js');

module.exports = function (req, res, next, data){
    res.render('menu', data, function (err, html) {
        if(!err){
            res.write(pagelet.wrapper('menu', html));
        }
    });
}