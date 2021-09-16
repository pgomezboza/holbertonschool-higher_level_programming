#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, (e, r) => {
  if (e) {
    console.log(e);
  } else {
    console.log('code: ' + r.statusCode);
  }
});
