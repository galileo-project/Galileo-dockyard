'use strict';

var pagelet = require('../../../utils/pagelet.js');

module.exports = function (req, res, next, data){
    res.render('notfoundLayout', data, function (err, html) {
        if(!err){
            res.write(html);
        }
    });
}