#!/usr/bin/node
const { argv } = require('process');

const Arguments = argv[2];
if (Arguments === undefined) {
  console.log('No argument');
} else {
  console.log(Arguments);
}
