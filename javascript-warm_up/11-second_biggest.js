#!/usr/bin/node
const { argv } = require('process');
const array = [];

if (argv[2] === undefined) {
  console.log(0);
} else {
  let count = 0;
  for (let i = 2; argv[i]; i++) {
    const number = parseInt(argv[i]);
    array.push(number);
    count += 1;
  } if (count === 1) {
    console.log(0);
  } else {
    array.sort(function (a, b) {
      return a - b;
    });
    console.log(array[count - 2]);
  }
}
