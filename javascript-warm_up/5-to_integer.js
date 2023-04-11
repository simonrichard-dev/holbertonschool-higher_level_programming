#!/usr/bin/node
const { argv } = require('process');

const number = parseInt(argv[2]);

if (Number.isInteger(number)) {
  console.log(number);
} else {
  console.log('Not a number');
}
