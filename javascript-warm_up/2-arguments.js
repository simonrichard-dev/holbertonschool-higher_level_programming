#!/usr/bin/node
const { argv } = require('process');

const Arguments = argv.length;

if (Arguments === 2) {
  console.log('No argument');
} else if (Arguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
