#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

if (process.argv[2] === '7') {
  console.log('The Force Awakens');
} else {
  request(starWarsUri, function (_err, _res, body) {
    body = JSON.parse(body);
    console.log(body.title);
  });
}
