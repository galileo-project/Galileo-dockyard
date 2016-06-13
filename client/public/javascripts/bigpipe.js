function getElementById(id) {
    return document.getElementById(id);
}

function BigPipe() {
    
}

BigPipe.prototype.set = function (id, html) {
    var element = getElementById(id);
    element.innerHTML = html; 
}

var bigPipe = BigPipe();