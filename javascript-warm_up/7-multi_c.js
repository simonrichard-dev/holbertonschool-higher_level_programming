#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);
const array = ['C is fun'];

if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log(array[0]);
  }
} else {
  console.log('Missing number of occurrences');
}
