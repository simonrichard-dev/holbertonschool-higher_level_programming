#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const Tasks = JSON.parse(body);
    const len = Tasks.length;
    const ListUsers = {};
    for (let i = 0; i < len; i++) {
      if (Tasks[i].completed === true) {
        if (ListUsers[Tasks[i].userId]) {
          ListUsers[Tasks[i].userId]++;
        } else {
          ListUsers[Tasks[i].userId] = 1;
        }
      }
    }
    console.log(ListUsers);
  }
});
