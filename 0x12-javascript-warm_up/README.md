# Javascript - Warm up

# Learning Objectives

* How to run a Javascript script
* How to create variables and constants
* What are differences between `var`, `const` and `let`
* What are all the data types available in Javascript
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use `while` and `for` loops
* How to use `break` and `continue` statements
* What is a function and how do you use functions
* What does a function that does not use any `return` statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

# Tasks

## First constant, first print

Write a script that prints “Javascript is amazing”:

* You must create a constant variable called `myVar` with the value “Javascript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [0-javascript_is_amazing.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/0-javascript_is_amazing.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
Javascript is amazing
$ amonkeyprogrammer@ubuntu:~/0x12$ 
$ amonkeyprogrammer@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## 3 languages

Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “Javascript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [1-multi_languages.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/1-multi_languages.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
Javascript is amazing
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Arguments

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [2-arguments.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/2-arguments.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./2-arguments.js 
No argument
$ amonkeyprogrammer@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
$ amonkeyprogrammer@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Value of my argument

Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

**Solution:** [3-value_argument.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/3-value_argument.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
$ amonkeyprogrammer@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Create a sentence

Write a script that prints two arguments passed to it, in the following format: “ is ”

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [4-concat.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/4-concat.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
$ amonkeyprogrammer@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
$ amonkeyprogrammer@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## An Integer

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

**Solution:** [5-to_integer.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/5-to_integer.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
$ amonkeyprogrammer@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
$ amonkeyprogrammer@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
$ amonkeyprogrammer@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
$ amonkeyprogrammer@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Loop to languages

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “Javascript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

**Solution:** [6-multi_languages_loop.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/6-multi_languages_loop.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
Javascript is amazing
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## I love C

Write a script that prints `x` times “C is fun”

* Where `x` is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only two `console.log`
* You must use a loop (`while`, `for`, etc.)

**Solution:** [7-multi_c.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/7-multi_c.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
$ amonkeyprogrammer@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ amonkeyprogrammer@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
$ amonkeyprogrammer@ubuntu:~/0x12$ ./7-multi_c.js -3
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Square

Write a script that prints a square

* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

**Solution:** [8-square.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/8-square.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./8-square.js
Missing size
$ amonkeyprogrammer@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
$ amonkeyprogrammer@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
$ amonkeyprogrammer@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ amonkeyprogrammer@ubuntu:~/0x12$ ./8-square.js -3
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Add

Write a script that prints the addition of 2 integers

* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [9-add.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/9-add.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./9-add.js 
NaN
$ amonkeyprogrammer@ubuntu:~/0x12$ ./9-add.js 1
NaN
$ amonkeyprogrammer@ubuntu:~/0x12$ ./9-add.js 1 7
8
$ amonkeyprogrammer@ubuntu:~/0x12$ ./9-add.js 13 89
102
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Factorial

Write a script that computes and prints a factorial

* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* You must do it recursively
* You must use a function
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [10-factorial.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/10-factorial.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./10-factorial.js 
1
$ amonkeyprogrammer@ubuntu:~/0x12$ ./10-factorial.js 3
6
$ amonkeyprogrammer@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
$ amonkeyprogrammer@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Second biggest!

Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

**Solution:** [11-second_biggest.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/11-second_biggest.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ ./11-second_biggest.js 
0
$ amonkeyprogrammer@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
$ amonkeyprogrammer@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Object

Update this script to replace the value `12` with `89`:

* You are not allowed to use `var`

**Solution:** [12-object.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/12-object.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

$ amonkeyprogrammer@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Add file

Write a function that returns the addition of 2 integers.

* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`

**Solution:** [13-add.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/13-add.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
$ amonkeyprogrammer@ubuntu:~/0x12$ ./13-main.js
8
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Const or not const

Write a file that modifies the value of `myVar` to `333`

**Solution:** [100-let_me_const.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/100-let_me_const.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
$ amonkeyprogrammer@ubuntu:~/0x12$ ./100-main.js
333
$ amonkeyprogrammer@ubuntu:~/0x12$
```

## Call me Moby

Write a function that executes `x` times a function.

* The function must be visible from outside
* Prototype: `function (x, theFunction)`
* You are not allowed to use `var`

**Solution:** [101-call_me_moby.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/101-call_me_moby.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
$ amonkeyprogrammer@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
$ amonkeyprogrammer@ubuntu:~/0x12$ 
```

## Add me maybe

Write a function that increments and calls a function.

* The function must be visible from outside
* Prototype: `function (number, theFunction)`
* You are not allowed to use `var`

**Solution:** [102-add_me_maybe.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/102-add_me_maybe.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
$ amonkeyprogrammer@ubuntu:~/0x12$ ./102-main.js
New value: 5
$ amonkeyprogrammer@ubuntu:~/0x12$ 
```

## Increment object

Update this script by adding a new function `incr` that increments the integer `value`.

* You are not allowed to use `var`

**Solution:** [103-object_fct.js](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x12-javascript-warm_up/103-object_fct.js)

```
$ amonkeyprogrammer@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

$ amonkeyprogrammer@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
$ amonkeyprogrammer@ubuntu:~/0x12$
```
