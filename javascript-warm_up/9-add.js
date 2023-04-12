#!/usr/bin/node
const { argv } = require('process');
const number1 = parseInt(argv[2]);
const number2 = parseInt(argv[3]);

const x = add(number1, number2);

function add (a, b) {
  return a * b;
}

console.log(x);
