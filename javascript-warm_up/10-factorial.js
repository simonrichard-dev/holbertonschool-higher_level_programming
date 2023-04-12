#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);

const answer = factorial(number);

function factorial (n) 
{
  if (Number.isInteger(number)) {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  } else {
    const number = 1
    return number;
  }
}

console.log(answer);
