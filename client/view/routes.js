var express = require('express');
var router = express.Router();

var home = require('./handler/home.js');
var login = require('./handler/login.js');
var error = require('./handler/error.js');
var manager = require('./handler/manager/index.js');


router.get('/',                 home.home);
router.get('/login',            login.login);

router.get('/manager/login',    manager.login);
router.get('/manager',          manager.home);

router.get('/*',                error.notfound);

module.exports = router;
