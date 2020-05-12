#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/';
const param = process.argv[2];

if (parseInt(param)) {
  request(starWarsUri.concat(param), function (_err, _res, body) {
    body = JSON.parse(body);
    console.log(body.title);
  });
} else {
  console.log('404 NOT FOUND');
}
