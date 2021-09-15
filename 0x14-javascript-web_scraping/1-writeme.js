#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];

fs.writeFile(file, str, 'utf8', (e) => {
  if (e) {
    console.log(e);
  }
});
