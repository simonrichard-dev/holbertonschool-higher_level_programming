#!/usr/bin/node
const { argv } = require('process');
const number = parseInt(argv[2]);

if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
