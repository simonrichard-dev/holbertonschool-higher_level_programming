#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response) {
  if (!error) {
    console.log('code:', response.statusCode);
  }
});
