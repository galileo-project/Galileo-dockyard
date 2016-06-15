'use strict';

module.exports = function (req, res, next, data){
    res.render('manager/layoutLogin', data, function (err, html) {
        if(!err){
            res.write(html);
        }
    });
}