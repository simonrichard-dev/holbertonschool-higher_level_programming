#!/usr/bin/node
const path = process.argv[2];
const Te = process.argv[3];
const fs = require('fs');

fs.writeFile(path, Te, 'utf-8', (err) => {
  if (err);
});
