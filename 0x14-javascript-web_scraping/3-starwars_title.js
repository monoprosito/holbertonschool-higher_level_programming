#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (_err, res, body) {
  body = JSON.parse(body);

  if (body.detail) {
    console.log(res.statusCode + ' ' + body.detail.toUpperCase());
  } else {
    console.log(body.title);
  }
});
