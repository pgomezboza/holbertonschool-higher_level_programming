#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”.

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    for (const n in data) {
      request.get(data[n], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const charName = JSON.parse(body).name;
          console.log(charName);
        }
      });
    }
  }
});
