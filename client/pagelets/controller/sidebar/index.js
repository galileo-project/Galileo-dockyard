'use strict';

var pagelet = require('../../../utils/pagelet.js');

module.exports = function (req, res, next, data){
    res.render('sidebar', data, function (err, html) {
        if(!err){
            res.write(pagelet.wrapper('sidebar', html));
        }
    });
}