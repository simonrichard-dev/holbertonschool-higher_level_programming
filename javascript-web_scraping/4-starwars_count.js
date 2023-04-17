#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const Films = JSON.parse(body);
    const len = Films.results.length;
    let count = 0;
    for (let i = 0; i < len; i++) {
      const char = Films.results[i].characters;
      for (let j = 0; j < char.length; j++) {
        const regex = '18';
        if (char[j].match(regex)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
