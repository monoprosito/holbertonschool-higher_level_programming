# Data Structures: Lists, Tuples

# Learning Objectives

* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it

# Tasks

## Print a list of integers

Write a function that prints all integers of a list.

* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Solution:** [0-print_list_integer.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/0-print_list_integer.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ amonkeyprogrammer@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Secure access to an element in a list

Write a function that retrieves an element from a list like in C.

* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative, the function should return `None`
* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
* You are not allowed to import any module
* You are not allowed to use `try/except`

**Solution:** [1-element_at.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/1-element_at.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

$ amonkeyprogrammer@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Replace element

Write a function that replaces an element of a list at a specific position (like in C).

* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative, the function should not modify anything, and returns the original list
* If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use `try/except`

**Solution:** [2-replace_in_list.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/2-replace_in_list.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

$ amonkeyprogrammer@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Print a list of integers... in reverse!

Write a function that prints all integers of a list, in reverse order.

* Prototype: `def print_reversed_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Solution:** [3-print_reversed_list_integer.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/3-print_reversed_list_integer.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

$ amonkeyprogrammer@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

* Prototype: `def new_in_list(my_list, idx, element):`
* If `idx` is negative, the function should return a copy of the original `list`
* If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
* You are not allowed to import any module
* You are not allowed to use `try/except`

**Solution:** [4-new_in_list.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/4-new_in_list.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

$ amonkeyprogrammer@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Can you C me now?

Write a function that removes all characters c and C from a string.

* Prototype: `def no_c(my_string):`
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use `str.replace()`

**Solution:** [5-no_c.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/5-no_c.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

$ amonkeyprogrammer@ubuntu:~/0x03$ ./5-main.py
Holberton Shool
hiago
 is fun!
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Lists of lists = Matrix

Write a function that prints a matrix of integers.

* Prototype: `def print_matrix_integer(matrix=[[]]):`
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Solution:** [6-print_matrix_integer.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/6-print_matrix_integer.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

$ amonkeyprogrammer@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Tuples addition

Write a function that adds 2 tuples.

* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
    * The first element should be the addition of the first element of each argument
    * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value `0` for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

**Solution:** [7-add_tuple.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/7-add_tuple.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

$ amonkeyprogrammer@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## More returns!

Write a function that returns a tuple with the length of a string and its first character.

* Prototype: `def multiple_returns(sentence):`
* If the sentence is empty, the first character should be equal to `None`
* You are not allowed to import any module

**Solution:** [8-multiple_returns.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/8-multiple_returns.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

$ amonkeyprogrammer@ubuntu:~/0x03$ ./8-main.py
Length: 32 - First character: A
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Find the max

Write a function that finds the biggest integer of a list.

* Prototype: `def max_integer(my_list=[]):`
* If the list is empty, return `None`
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin `max()`

**Solution:** [9-max_integer.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/9-max_integer.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

$ amonkeyprogrammer@ubuntu:~/0x03$ ./9-main.py
Max: 90
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Only by 2

Write a function that finds all multiples of 2 in a list.

* Prototype: `def divisible_by_2(my_list=[]):`
* Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

**Solution:** [10-divisible_by_2.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/10-divisible_by_2.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

$ amonkeyprogrammer@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Delete at

Write a function that deletes the item at a specific position in a list.

* Prototype: `def delete_at(my_list=[], idx=0):`
* If `idx` is negative or out of range, nothing change (returns the same list)
* You are not allowed to use `pop()`
* You are not allowed to import any module

**Solution:** [11-delete_at.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/11-delete_at.py)

```
$ amonkeyprogrammer@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

$ amonkeyprogrammer@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
$ amonkeyprogrammer@ubuntu:~/0x03$
```

## Switch

Complete the source code in order to switch value of `a` and `b`

* You can find the source code [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long

**Solution:** [12-switch.py](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/12-switch.py)

```
$ amonkeyprogrammer@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
$ amonkeyprogrammer@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
$ amonkeyprogrammer@ubuntu:~/py/0x03$
```

## Linked list palindrome (C programming language)

Write a function in C that checks if a singly linked list is a palindrome.

* Prototype: `int is_palindrome(listint_t **head);`
* Return: `0` if it is not a palindrome, `1` if it is a palindrome
* An empty list is considered a palindrome

```
$ amonkeyprogrammer@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
$ amonkeyprogrammer@ubuntu:0x03$
```

```
$ amonkeyprogrammer@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
$ amonkeyprogrammer@ubuntu:0x03$
```

```
$ amonkeyprogrammer@ubuntu:0x03$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
$ amonkeyprogrammer@ubuntu:0x03$
```

**Solution:** [13-is_palindrome.c](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/13-is_palindrome.c), [lists.h](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/lists.h)

```
$ amonkeyprogrammer@ubuntu:0x03$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
$ amonkeyprogrammer@ubuntu:0x03$
```

## CPython #0: Python lists

CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.

Create a C function that prints some basic info about Python lists.

* Prototype: `void print_python_list_info(PyObject *p);`
* Format: see example
* Python version: 3.4
* Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
* OS: `Ubuntu 14.04 LTS`

**Solution:** [100-print_python_list_info.c](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x03-python-data_structures/100-print_python_list_info.c)

```
$ amonkeyprogrammer@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
$ amonkeyprogrammer@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
$ amonkeyprogrammer@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
$ amonkeyprogrammer@CPython:~/CPython$
```
