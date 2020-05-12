#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (err, _res, body) {
  if (err == null) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
