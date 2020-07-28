# Web jQuery

# Learning Objectives

* How to select HTML elements with jQuery
* What are differences between `ID`, `class` and `tag name` selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a `GET` request with jQuery Ajax
* How to make a `POST` request with jQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

# Tasks

## No jQuery

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

* You must use `document.querySelector` to select the HTML tag
* You can’t use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [0-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/0-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## With jQuery

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [1-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/1-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Click and turn red

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [2-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/2-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Add `.red` class

Write a Javascript script that adds the class `red` to the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [3-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/3-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Toggle classes

Write a Javascript script that toggles the class of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#toggle_header`:

* The `HEADER` tag must always have one class: `red` or `green`, never both in the same time, never empty.
* If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green`; and the reverse.
* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [4-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/4-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## List of elements

Write a Javascript script that adds a `LI` element to a list when the user clicks on the tag `DIV#add_item`:

* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [5-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/5-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Change the text

Write a Javascript script that updates the text of the HTML tag `HEADER` to “New Header!!!” when the user clicks on `DIV#update_header`

* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [6-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/6-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Star wars character

Write a Javascript script that fetches and replaces the `name` of this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

* The name must be displayed in the HTML tag `DIV#character`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [7-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/7-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Star Wars movies

Write a Javascript script that fetches and lists all movies title by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

* All movie titles must be list in the HTML tag `UL#list_movies`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:

**Solution:** [8-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/8-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```

## Say Hello!

Write a Javascript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML’s tag `DIV#hello`.

* The translation of “hello” must be display in the HTML tag `DIV#hello`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the jQuery API
* Your script must work when it is imported from the `HEAD` tag

Please test with this HTML file in your browser:

**Solution:** [9-script.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/9-script.js)

```
$ amonkeyprogrammer@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
$ amonkeyprogrammer@ubuntu:~/0x15$
```
