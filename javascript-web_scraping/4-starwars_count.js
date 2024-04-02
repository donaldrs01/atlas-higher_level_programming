#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
const charID = 18;

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  /* Prase JSON resposne, search for films with specific charID and assign var,
    print length of var */
  // Specifically parse the 'results' listing on the page
  const films = JSON.parse(body).results;
  // Use filter() to filter film array by searching for 'characters' that incluke charID 18
  const wedgeFilms = films.filter(film => {
    return film.characters.some(character => character.includes(`/api/people/${charID}/`));
  });
  // Print length of wedgeFilms array
  console.log(wedgeFilms.length);
});
