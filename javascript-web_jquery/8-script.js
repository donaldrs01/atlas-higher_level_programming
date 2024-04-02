/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    // Extract movies from fetched data
    const movieList = data.results;
    // forEach() iterates through list and collects titles
    movieList.forEach(film => {
      const title = film.title;
      // append new <li> element with movie title
      $('#list_movies').append('<li>' + title + '</li>');
    });
  });
});
