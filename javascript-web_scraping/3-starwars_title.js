#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const urlPath = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

request(urlPath, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    // Convert JSON response from API into JS-compatible object
    const film = JSON.parse(body);
    // Use dot notation to access object attributes (film title)
    console.log(film.title);
});
