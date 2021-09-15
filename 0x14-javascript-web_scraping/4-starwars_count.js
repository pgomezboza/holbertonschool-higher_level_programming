#!/usr/bin/node
// script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log('error:', err);
  } else {
    const resjson = JSON.parse(body);
    const res = resjson.results;

    let count = 0;
    for (let n = 0; n < res.length; n++) {
      const chars = (res[n].characters);
      for (let m = 0; m < chars.length; m++) {
        const charId = chars[m].includes('18');
        if (charId) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
