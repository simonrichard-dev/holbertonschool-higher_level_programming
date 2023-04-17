#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/',
  function (error, body) {
    if (!error) {
      const Film = JSON.parse(body);
      console.log(Film.title);
    }
  });
