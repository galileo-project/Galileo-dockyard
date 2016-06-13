'use strict';

function wrapper(id, html) {
    var data = '\n<script> bigPipeSet(\'' + id + '\' , \'' + html + '\')</script>'
    return data;
}

module.exports = {
    wrapper: wrapper
}