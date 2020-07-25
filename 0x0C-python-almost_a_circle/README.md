# Almost a Circle

# Learning Objectives

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

# Tasks

## If it's not tested it doesn't work

All your files, classes and methods must be unit tested and be PEP 8 validated.

```
$ amonkeyprogramer@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 31 tests in 13.135s

OK
$ amonkeyprogramer@ubuntu:~/$
```

## Base class

Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python module

Create a file named `models/base.py`:

* Class `Base`:
    * private class attribute `__nb_objects = 0`
    * class constructor: `def __init__(self, id=None):`:
        * if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
        * otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

**Solution:** [models/base.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py), [models/__init__.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/__init__.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

$ amonkeyprogramer@ubuntu:~/$ ./0-main.py
1
2
3
12
4
$ amonkeyprogramer@ubuntu:~/$
```

## First Rectangle

Write the class `Rectangle` that inherits from `Base`:

* In the file `models/rectangle.py`
* Class `Rectangle` inherits from `Base`
* Private instance attributes, each with its own public getter and setter:
    * `__width` -> `width`
    * `__height` -> `height`
    * `__x` -> `x`
    * `__y` -> `y`
* Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
    * all the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
    * Assign each argument `width`, `height`, `x` and `y` to the right attribute

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

$ amonkeyprogramer@ubuntu:~/$ ./1-main.py
1
2
12
$ amonkeyprogramer@ubuntu:~/$
```

## Validate attributes

Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

* If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
* If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
* If `x` or y is under 0, raise the ValueError exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

$ amonkeyprogramer@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
$ amonkeyprogramer@ubuntu:~/$
```

## Area first

Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

$ amonkeyprogramer@ubuntu:~/$ ./3-main.py
6
20
56
$ amonkeyprogramer@ubuntu:~/$
```

## Display #0

Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle x and y here.

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

$ amonkeyprogramer@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
$ amonkeyprogramer@ubuntu:~/$
```

## __str__

Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

$ amonkeyprogramer@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
$ amonkeyprogramer@ubuntu:~/$
```

## Display #1

Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the Rectangle instance with the character `#` by taking care of `x` and `y`

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

$ amonkeyprogramer@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
$ amonkeyprogramer@ubuntu:~/$
```

## Update #0

Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

* 1st argument should be the `id` attribute
* 2nd argument should be the `width` attribute
* 3rd argument should be the `height` attribute
* 4th argument should be the `x` attribute
* 5th argument should be the `y` attribute

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

$ amonkeyprogramer@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
$ amonkeyprogramer@ubuntu:~/$
```

## Update #1

Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

* `**kwargs` can be thought of as a double pointer to a dictionary: key/value
    * As Python doesn’t have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
* `**kwargs` must be skipped if `*args` exists and is not empty
* Each key in this dictionary represents an attribute to the instance

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

$ amonkeyprogramer@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
$ amonkeyprogramer@ubuntu:~/$
```

## And now, the Square!

Write the class `Square` that inherits from `Rectangle`:

* In the file `models/square.py`
* Class `Square` inherits from `Rectangle`
* Class constructor: `def __init__(self, size, x=0, y=0, id=None):`:
    * Call the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the `Rectangle` class. The `width` and `height` must be assigned to the value of `size`
    * You must not create new attributes for this class, use all attributes of `Rectangle` - As reminder: a Square is a Rectangle with the same width and height
    * All `width`, `height`, `x` and `y` validation must inherit from `Rectangle` - same behavior in case of wrong data
* The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height`

**Solution:** [models/square.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

$ amonkeyprogramer@ubuntu:~/$ ./9-main.py
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
  ##
  ##
---
[Square] (3) 1/3 - 3
9



 ###
 ###
 ###
$ amonkeyprogramer@ubuntu:~/$
```

## Square size

Update the class `Square` by adding the public getter and setter `size`

* The setter should assign (in this order) the `width` and the `height` - with the same value
* The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`)

**Solution:** [models/square.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

$ amonkeyprogramer@ubuntu:~/$ ./10-main.py
[Square] (1) 0/0 - 5
5
[Square] (1) 0/0 - 10
[TypeError] width must be an integer
$ amonkeyprogramer@ubuntu:~/$
```

## Square update

Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:

* `*args` is the list of arguments - no-keyworded arguments
    * 1st argument should be the `id` attribute
    * 2nd argument should be the `size` attribute
    * 3rd argument should be the `x` attribute
    * 4th argument should be the `y` attribute
* `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
* `**kwargs` must be skipped if *args exists and is not empty
* Each key in this dictionary represents an attribute to the instance

**Solution:** [models/square.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

$ amonkeyprogramer@ubuntu:~/$ ./11-main.py
[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
$ amonkeyprogramer@ubuntu:~/$
```

## Rectangle instance to dictionary representation

Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`:

This dictionary must contain:

* `id`
* `width`
* `height`
* `x`
* `y`

**Solution:** [models/rectangle.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

$ amonkeyprogramer@ubuntu:~/$ ./12-main.py
[Rectangle] (1) 1/9 - 10/2
{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
<class 'dict'>
[Rectangle] (2) 0/0 - 1/1
[Rectangle] (1) 1/9 - 10/2
False
$ amonkeyprogramer@ubuntu:~/$
```

## Square instance to dictionary representation

Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`:

This dictionary must contain:

* `id`
* `size`
* `x`
* `y`

**Solution:** [models/square.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 13-main.py
#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

$ amonkeyprogramer@ubuntu:~/$ ./13-main.py
[Square] (1) 2/1 - 10
{'id': 1, 'x': 2, 'size': 10, 'y': 1}
<class 'dict'>
[Square] (2) 1/0 - 1
[Square] (1) 2/1 - 10
False
$ amonkeyprogramer@ubuntu:~/$
```

## Dictionary to JSON string

JSON is one of the standard formats for sharing data representation.

Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`:

* `list_dictionaries` is a list of dictionaries
* If `list_dictionaries` is `None` or empty, return the string: `"[]"`
* Otherwise, return the JSON string representation of `list_dictionaries`

**Solution:** [models/base.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 14-main.py
#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

$ amonkeyprogramer@ubuntu:~/$ ./14-main.py
{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
<class 'dict'>
[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
<class 'str'>
$ amonkeyprogramer@ubuntu:~/$
```

## JSON string to file

Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file:

* `list_objs` is a list of instances who inherits of Base - example: list of Rectangle or list of Square instances
* If `list_objs` is `None`, save an empty list
* The filename must be: `<Class name>.json` - example: `Rectangle.json`
* You must use the static method `to_json_string` (created before)
* You must overwrite the file if it already exists

**Solution:** [models/base.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 15-main.py
#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

$ amonkeyprogramer@ubuntu:~/$ ./15-main.py
[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
$ amonkeyprogramer@ubuntu:~/$
```

## JSON string to dictionary

Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`:

* `json_string` is a string representing a list of dictionaries
* If `json_string` is `None` or empty, return an empty list
* Otherwise, return the list represented by `json_string`

**Solution:** [models/base.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 16-main.py
#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

$ amonkeyprogramer@ubuntu:~/$ ./16-main.py
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
[<class 'str'>] [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
$ amonkeyprogramer@ubuntu:~/$
```

## Dictionary to Instance

Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set:

* `**dictionary` can be thought of as a double pointer to a dictionary
* To use the `update` method to assign all attributes, you must create a “dummy” instance before:
    * Create a `Rectangle` or `Square` instance with “dummy” mandatory attributes (width, height, size, etc.)
    * Call `update` instance method to this “dummy” instance to apply your real values
* You must use the method `def update(self, *args, **kwargs)`
* `**dictionary` must be used as `**kwargs` of the method `update`
* You are not allowed to use `eval`

**Solution:** [models/base.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 17-main.py
#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

$ amonkeyprogramer@ubuntu:~/$ ./17-main.py
[Rectangle] (1) 1/0 - 3/5
[Rectangle] (1) 1/0 - 3/5
False
False
$ amonkeyprogramer@ubuntu:~/$
```

## File to instances

Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances:

* The filename must be: `<Class name>.json` - example: `Rectangle.json`
* If the file doesn’t exist, return an empty list
* Otherwise, return a list of instances - the type of these instances depends on `cls` (current class using this method)
* You must use the `from_json_string` and `create` methods (implemented previously)

**Solution:** [models/base.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)

```
$ amonkeyprogramer@ubuntu:~/$ cat 18-main.py
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

$ amonkeyprogramer@ubuntu:~/$ ./18-main.py
[139785912033120] [Rectangle] (1) 2/8 - 10/7
[139785912033176] [Rectangle] (2) 0/0 - 2/4
---
[139785911764752] [Rectangle] (1) 2/8 - 10/7
[139785911764808] [Rectangle] (2) 0/0 - 2/4
---
---
[139785912058040] [Square] (5) 0/0 - 5
[139785912061848] [Square] (6) 9/1 - 7
---
[139785911764976] [Square] (5) 0/0 - 5
[139785911765032] [Square] (6) 9/1 - 7
$ amonkeyprogramer@ubuntu:~/$
```
