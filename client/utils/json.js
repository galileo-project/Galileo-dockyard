'use strict';


function extendJson() {
    var sources = [].slice.call(arguments);
    var target  = {};
    
    if(!sources[0]){
        return sources[1];
    } else if(!sources[1]) {
        return sources[0];
    };

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