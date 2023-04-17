#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  console.log('code: ', response.statusCode);
});
