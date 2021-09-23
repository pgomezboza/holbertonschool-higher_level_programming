// script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
let movie;

$.get(url, function (data) {
  for (movie of data.results) {
    $('UL#list_movies').append($('<li></li>').text(movie.title));
  }
});
