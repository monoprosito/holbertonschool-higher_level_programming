#!/usr/bin/node

const request = require('request');

async function get (url, options) {
  return new Promise(function (resolve, reject) {
    request.get(url, options, function (err, res) {
      if (err) {
        reject(err);
      } else {
        resolve(res);
      }
    });
  });
}

async function post (url, options) {
  return new Promise(function (resolve, reject) {
    request.post(url, options, function (err, res) {
      if (err) {
        reject(err);
      } else {
        resolve(res);
      }
    });
  });
}

async function bearerToken () {
  const consumerKey = process.argv[2];
  const consumerSecretKey = process.argv[3];
  const consumerKeys = `${consumerKey}:${consumerSecretKey}`;
  const encodedConsumerKeys = Buffer.from(consumerKeys).toString('base64');
  const bearerTokenUrl = 'https://api.twitter.com/oauth2/token';
  const requestConfig = {
    url: bearerTokenUrl,
    Authorization: `Basic ${encodedConsumerKeys}`,
    auth: {
      user: consumerKey,
      pass: consumerSecretKey
    },
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    form: {
      grant_type: 'client_credentials'
    }
  };

  const response = await post(requestConfig);
  const body = response.body;

  if (response.statusCode !== 200) {
    const error = body.errors.pop();
    throw Error(`Error ${error.code}: ${error.message}`);
  }

  return JSON.parse(response.body).access_token;
}

async function getAllTweetsByUser (token, user) {
  const requestConfig = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    auth: {
      bearer: token
    },
    qs: {
      q: user,
      count: '5',
      result_type: 'recent'
    }
  };

  const response = await get(requestConfig);

  if (response.statusCode !== 200) {
    throw new Error(response.body);
  }

  return JSON.parse(response.body);
}

(async () => {
  let token;

  try {
    // Exchange the credentials for a Bearer token
    token = await bearerToken();
  } catch (e) {
    console.error(`Could not generate a Bearer token. Please check that your credentials are correct and that the Filtered Stream preview is enabled in your Labs dashboard. (${e})`);
    process.exit(-1);
  }

  try {
    const tweets = await getAllTweetsByUser(token, process.argv[4]);

    for (let i = 0; i < tweets.statuses.length; ++i) {
      const tweetId = tweets.statuses[i].id;
      const tweetText = tweets.statuses[i].text;
      const tweetOwner = tweets.statuses[i].user.name;

      console.log(`[${tweetId}] ${tweetText} by ${tweetOwner}`);
    }
  } catch (e) {
    console.error(e);
    process.exit(-1);
  }
})();
