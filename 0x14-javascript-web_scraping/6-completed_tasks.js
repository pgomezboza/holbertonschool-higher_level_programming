#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const dict = {};
    for (let n = 0; n < todos.length; n++) {
      const status = (todos[n].completed);
      const key = todos[n].userId.toString();
      if (status) {
        if (dict[key]) {
          dict[key]++;
        } else {
          dict[key] = 1;
        }
      }
    }
    console.log(dict);
  }
});
