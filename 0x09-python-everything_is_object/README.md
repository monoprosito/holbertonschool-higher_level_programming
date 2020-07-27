# Everything is object

# Learning Objectives

* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions

# Tasks

## Who am I?

What function would you use to print the type of an object?

**Solution:** [0-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/0-answer.txt)

## Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementation)?

**Solution:** [1-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/1-answer.txt)

## Right count

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

**Solution:** [2-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/2-answer.txt)

```
>>> a = 89
>>> b = 100
```

## Right count =

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

**Solution:** [3-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/3-answer.txt)

```
>>> a = 89
>>> b = 89
```

## Right count =

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

**Solution:** [4-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/4-answer.txt)

```
>>> a = 89
>>> b = a
```

## Right count =+

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

**Solution:** [5-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/5-answer.txt)

```
>>> a = 89
>>> b = a + 1
```

## Is equal

What do these 3 lines print?

**Solution:** [6-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/6-answer.txt)

```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

## Is the same

What do these 3 lines print?

**Solution:** [7-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/7-answer.txt)

```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

## Is really equal

What do these 3 lines print?

**Solution:** [8-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/8-answer.txt)

```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

## Is really the same

What do these 3 lines print?

**Solution:** [9-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/9-answer.txt)

```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

## And with a list, is it equal

What do these 3 lines print?

**Solution:** [10-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/10-answer.txt)

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

## And with a list, is it the same

What do these 3 lines print?

**Solution:** [11-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/11-answer.txt)

```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

## And with a list, is it really equal

What do these 3 lines print?

**Solution:** [12-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/12-answer.txt)

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

## And with a list, is it really the same

What do these 3 lines print?

**Solution:** [13-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/13-answer.txt)

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

## List append

What does this script print?

**Solution:** [14-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/14-answer.txt)

```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

## List add

What does this script print?

**Solution:** [15-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/15-answer.txt)

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

## Integer incrementation

What does this script print?

**Solution:** [16-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/16-answer.txt)

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

## List incrementation

What does this script print?

**Solution:** [17-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/17-answer.txt)

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

## List assignation

What does this script print?

**Solution:** [18-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/18-answer.txt)

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

## Copy a list object

Write a function `def copy_list(l):` that returns a **copy** of a list.

* The input list can contain any type of objects
* Your file should be maximum 3-line long (no documentation needed)
* You are not allowed to import any module

**Solution:** [19-copy_list.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/19-copy_list.py)

```
$ amonkeyprogrammer@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

$ amonkeyprogrammer@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
$ amonkeyprogrammer@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
$ amonkeyprogrammer@ubuntu:~/0x09$
```

## Tuple or not?

```
a = ()
```

Is `a` a tuple? Answer with `Yes` or `No`.

**Solution:** [20-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/20-answer.txt)

## Tuple or not?

```
a = (1, 2)
```

Is `a` a tuple? Answer with `Yes` or `No`.

**Solution:** [21-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/21-answer.txt)

## Tuple or not?

```
a = (1)
```

Is `a` a tuple? Answer with `Yes` or `No`.

**Solution:** [22-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/22-answer.txt)

## Tuple or not?

```
a = (1, )
```

Is `a` a tuple? Answer with `Yes` or `No`.

**Solution:** [23-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/23-answer.txt)

## Richard Sim's special #0

What does this script print?

**Solution:** [24-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/24-answer.txt)

```
a = (1)
b = (1)
a is b
```

## Richard Sim's special #1

What does this script print?

**Solution:** [25-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/25-answer.txt)

```
a = (1, 2)
b = (1, 2)
a is b
```

## Richard Sim's special #2

What does this script print?

**Solution:** [26-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/26-answer.txt)

```
a = ()
b = ()
a is b
```

## Richard Sim's special #3

```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

**Solution:** [27-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/27-answer.txt)

## Richard Sim's special #4

```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

**Solution:** [28-answer.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/28-answer.txt)

## #pythonic

Write a function `magic_string()` that returns a string “Holberton” n times the number of the iteration (see code):

* Format: see example
* Your file should be maximum 4-line long (no documentation needed)
* You are not allowed to import any module

**Solution:** [100-magic_string.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/100-magic_string.py)

```
$ amonkeyprogrammer@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

$ amonkeyprogrammer@ubuntu:~/0x09$ ./100-main.py | cat -e
Holberton$
Holberton, Holberton$
Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
$ amonkeyprogrammer@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
$ amonkeyprogrammer@ubuntu:~/0x09$
```

## Low memory cost

Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

* You are not allowed to import any module

**Solution:** [101-locked_class.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/101-locked_class.py)

```
$ amonkeyprogrammer@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ amonkeyprogrammer@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
$ amonkeyprogrammer@ubuntu:~/0x09$
```

## int 1/3

```
$ amonkeyprogrammer@ubuntu:/python3$ cat int.py 
a = 1
b = 1
$ amonkeyprogrammer@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

* How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
* How many int objects are created by the execution of the second line of the script (`103-line2.txt`)

**Solution:** [103-line1.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line1.txt), [103-line2.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line2.txt)

## int 2/3

```
$ amonkeyprogrammer@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
$ amonkeyprogrammer@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

* How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
* How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
* After the execution of line 3, is the int object pointed by `a` deleted? Answer with `Yes` or `No` (`104-line3.txt`)
* After the execution of line 4, is the int object pointed by `b` deleted? Answer with `Yes` or `No` (`104-line4.txt`)
* How many int objects are created by the execution of the last line of the script (`104-line5.txt`)

**Solution:** [104-line1.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line1.txt), [104-line2.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line2.txt), [104-line3.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line3.txt), [104-line4.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line4.txt), [104-line5.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/103-line5.txt)

## int 3/3

```
$ amonkeyprogrammer@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
$ amonkeyprogrammer@ubuntu:/tmp/so$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

* Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)

**Solution:** [105-line1.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/105-line1.txt)

## Clear strings

```
$ amonkeyprogrammer@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
$ amonkeyprogrammer@ubuntu:/python3$
```

Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

* How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
* How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
* After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
* After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
* How many string objects are created by the execution of the last line of the script (`106-line5.txt`)

**Solution:** [106-line1.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line1.txt), **Solution:** [106-line4.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line2.txt), **Solution:** [106-line3.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line3.txt), **Solution:** [106-line4.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line4.txt), **Solution:** [106-line5.txt](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/106-line5.txt), 
