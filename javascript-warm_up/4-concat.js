#!/usr/bin/node
const { argv } = require('process');

const language = argv[2];
const option = argv[3];
if (language === undefined) {
  console.log(language + ' is undefined');
} else if (option === undefined) {
  console.log(language + ' is undefined');
} else {
  console.log(language + ' is ' + option);
}
