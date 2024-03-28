#!/usr/bin/node
const request = require('request');
const urlPath = process.argv[2];

request(urlPath, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
