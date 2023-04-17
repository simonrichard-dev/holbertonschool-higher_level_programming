#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const GetLorem = process.argv[2];
const FileToWrite = process.argv[3];

request(GetLorem, function (error, response, body) {
  if (!error) {
    fs.writeFile(FileToWrite, body, 'utf-8', (err) => {
      if (err);
    });
  }
});
