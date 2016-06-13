var express = require('express');
var router = express.Router();

var home = require('./handler/home.js');

/* GET home page. */
router.get('/', home.home);

module.exports = router;
