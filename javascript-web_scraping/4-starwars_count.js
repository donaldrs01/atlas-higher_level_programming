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
})
