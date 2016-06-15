'use strict';


class BigPipe {
    constructor(req, res, next, status) {
        if(typeof status === 'undefined'){
            status = 200;
        }
        this._req    = req;
        this._res    = res;
        this._next   = next;
        this._status = status
        this.setHead()
    }

    setHead() {
        this._res.writeHead(this._status, {
            'Content-Type':      'text/html',
            'Transfer-Encoding': 'chunked'
        });
    }

    push(pagelet, data) {
        pagelet(this._req, this._res, this._next, data);
    }

    send(pagelet, data) {
        pagelet(this._req, this._res, this._next, data);
        this.finish(false);
    }

    finish(withTag) {
        if(withTag || typeof withTag === 'undefined'){
            this._res.end('</body></html>');
        } else {
            this._res.end();
        }
    }

    
}

module.exports = BigPipe;