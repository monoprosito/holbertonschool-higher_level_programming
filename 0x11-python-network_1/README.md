# Network #1

# Learning Objectives

* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` #requestsiswaysimplerthanurllib
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

# Tasks

## What's my status? #0

Write a Python script that fetches `https://intranet.hbtn.io/status`

* You must use the package `urllib`
* You are not allowed to import any packages other than `urllib`
* The body of the response must be displayed like the following example (tabulation before -)
* You must use a `with` statement

**Solution:** [0-hbtn_status.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/0-hbtn_status.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
$ amonkeyprogrammer@ubuntu:~/0x11$ 
```

## Response header value #0

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

* You must use the packages `urllib` and `sys`
* You are not allow to import packages other than `urllib` and `sys`
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a `with` statement

**Solution:** [1-hbtn_header.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/1-hbtn_header.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
$ amonkeyprogrammer@ubuntu:~/0x11$ 
$ amonkeyprogrammer@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## POST an email #0

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

* The email must be sent in the `email` variable
* You must use the packages `urllib` and `sys`
* You are not allowed to import packages other than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement

**Solution:** [2-post_email.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/2-post_email.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

* You have to manage `urllib.error.HTTPError` exceptions and print: `Error code`: followed by the HTTP status code
* You must use the packages `urllib` and `sys`
* You are not allowed to import other packages than `urllib` and `sys`
* You don’t need to check arguments passed to the script (number or type)
* You must use the `with` statement

**Solution:** [3-error_code.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/3-error_code.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
$ amonkeyprogrammer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ amonkeyprogrammer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ amonkeyprogrammer@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## What's my status? #1

Write a Python script that fetches `https://intranet.hbtn.io/status`

* You must use the package `requests`
* You are not allow to import packages other than `requests`
* The body of the response must be display like the following example (tabulation before `-`)

**Solution:** [4-hbtn_status.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/4-hbtn_status.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

* You must use the packages `requests` and `sys`
* You are not allow to import other packages than `requests` and `sys`
* The value of this variable is different for each request
* You don’t need to check script arguments (number and type)

**Solution:** [5-hbtn_header.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/5-hbtn_header.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
$ amonkeyprogrammer@ubuntu:~/0x11$ 
$ amonkeyprogrammer@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## POST an email #1

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

* The email must be sent in the variable `email`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to error check arguments passed to the script (number or type)

**Solution:** [6-post_email.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/6-post_email.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

* If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)

**Solution:** [7-error_code.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/7-error_code.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
$ amonkeyprogrammer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
$ amonkeyprogrammer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
$ amonkeyprogrammer@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## Search API

Write a Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

* The letter must be sent in the variable `q`
* If no argument is given, set `q=""`
* If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
* Otherwise:
    * Display `Not a valid JSON` if the JSON is invalid
    * Display `No result` if the JSON is empty
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`

**Solution:** [8-json_api.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/8-json_api.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./8-json_api.py 
No result
$ amonkeyprogrammer@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
$ amonkeyprogrammer@ubuntu:~/0x11$ ./8-json_api.py 2
No result
$ amonkeyprogrammer@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## My Github!

Write a Python script that takes your Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your `id`

* You must use [Basic Authentication](https://developer.github.com/v3/auth/#basic-authentication) with a [personal access token as password](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to access to your information (only `read:user` permission is needed)
* The first argument will be your username
* The second argument will be your password (in your case, a [personal access token as password](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token))
* You must use the package `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)

**Solution:** [10-my_github.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/10-my_github.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./10-my_github.py monoprosito random_pwd
6069359
$ amonkeyprogrammer@ubuntu:~/0x11$ ./10-my_github.py monoprosito wrong_pwd
None
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## Time for an interview!

```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the Github API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```

Write a Python script that takes 2 arguments in order to solve this challenge.

* The first argument will be the `repository name`
* The second argument will be the `owner name`
* You must use the packages `requests` and `sys`
* You are not allowed to import packages other than `requests` and `sys`
* You don’t need to check arguments passed to the script (number or type)

**Solution:** [100-github_commits.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/100-github_commits.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./100-github_commits.py rails rails
23229d24533218bbbef04eba0fca8809ad00f9d7: Eugene Kenny
ee9a1f8bdf0197cc535eba933c51a3534b692b41: Eugene Kenny
8eec6ee962915c528b4a8a124a4ce65fd115a374: Daniel Colson
ae37c17597f93bc49e3a67218a08b7d1265f640b: Eugene Kenny
5e2d3db4b5846db56728ddae63bb1eb9a14ed6d3: Jonathan Hefner
eb51286f6755a97daf2b046c04b83b794c418913: Ryuta Kamizono
75c309c7ad6517a7fad482f1efd50baadf4bdf45: Ryuta Kamizono
70c9f39039e790c65236a2057fdbcb34002dfa62: Eugene Kenny
396b43a99d436d87c409a1260d55141716ab7cd3: Victor Perez Rodriguez  
c14da7be2216e59cca788f3c40843a91624b3762: Gerard (Gerry) Caulfield
$ amonkeyprogrammer@ubuntu:~/0x11$
```

## Twitter Auth

Write a Python script that takes in 3 strings and sends a search request to the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index)

* Use the [Twitter API search endpoint](https://developer.twitter.com/en/docs/api-reference-index)
* Use the [Application-only authentication](https://developer.twitter.com/en/docs/basics/authentication/overview) flow to do a search request
* Create an Twitter application [here](https://developer.twitter.com/app)
* The first argument must be the Consumer Key (API Key)
* The second argument must be the Consumer Secret (API Secret)
* The third argument must be the search string
* Display only 5 results in the following format: `[<Tweet ID>] <Tweet text> by <Tweet owner name>` (see example below)
* You must use the packages `requests`, `base64` and `sys`
* You are not allowed to import packages other than `requests`, `base64` and `sys`
* You don’t need to check arguments passed to the script (number or type)

**Solution:** [103-search_twitter.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x11-python-network_1/103-search_twitter.py)

```
$ amonkeyprogrammer@ubuntu:~/0x11$ ./103-search_twitter.py CONSUMER_KEY CONSUMER_SECRET_KEY "#github"
[1287909672171732992] #git is #freesw 
#github is not free and not even open... except opening one's buttcheeks to #microsoft #ProprietarySoftware #monopoly by Dr. Roy Schestowitz (罗伊)
[1287907830536830977] RT @filippo: If want to combine the advantages of organizing your html/js/css in components with server-side rendering and you love writing… by Derrick Amenuve
[1287907319024517120] RT @SSW_TV: NEW VIDEO from #SSWTV is out! Is #Github the best Content Management System (#CMS)? Find out why GitHub might be great choice f… by Jernej Kavka (JK)
[1287906301272633349] RT @juelvaldivia: Les traigo algo histórico amigos
El código fuente del Apollo-11
#github

https://t.co/BUd93nHaaU by Iván Abascal
[1287906149606526976] RT @kerixa: Day 11 of #100DaysOfCode learned git and github. Worked with version control #udemy #github by Very Proud Robot
$ amonkeyprogrammer@ubuntu:~/0x11$
```
