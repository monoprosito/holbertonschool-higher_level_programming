#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_err, _res, body) {
  const completedTasksByUsers = {};
  let userId = 0;
  let completed = false;

  body = JSON.parse(body);

  for (let i = 0; i < body.length; ++i) {
    userId = body[i].userId;
    completed = body[i].completed;

    if (!completedTasksByUsers[userId]) {
      completedTasksByUsers[userId] = 0;
    }

    if (completed) ++completedTasksByUsers[userId];
  }

  console.log(completedTasksByUsers);
});
