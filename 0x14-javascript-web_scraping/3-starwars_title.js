#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (err, _res, body) {
  body = JSON.parse(body);

  if (body.title) {
    console.log(body.title);
  } else {
    console.log(err);
  }
});
