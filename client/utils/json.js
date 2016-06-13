'use strict';


function extendJson() {
    var sources = [].slice.call(arguments);
    var target  = {};
    sources.forEach(function (source) {
        for (var prop in source) {
            target[prop] = source[prop];
        }
    });
    return target;
}

module.exports = {
    extendJson:    extendJson
}