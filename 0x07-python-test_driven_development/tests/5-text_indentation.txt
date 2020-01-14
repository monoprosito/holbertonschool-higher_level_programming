===============================
4. Text indentation module
===============================

Import module:
==============
    >>> text_indentation = __import__('5-text_indentation').text_indentation


Function:
=========
Write a function that prints a text with 2 new lines after
each of these characters: ., ? and :


Notes:
===========
    * text must be a string, otherwise raise a TypeError exception
    with the message 'text must be a string'.

    * There should be no space at the beginning or at the
    end of each printed line.


Section // Non-Parameters
=========================

Test case #0: A test case without parameters

    >>> text_indentation()
    Traceback (most recent call last):
    TypeError: text_indentation() missing 1 required positional argument: 'text'


Section // Correct Parameters
=============================

Test case #1: A test case with a short text

    >>> text_indentation('Monty Python')
    Monty Python

Test case #2: A test case with a short text and a character for 2 new lines

    >>> text_indentation('Ponty Mython?')
    Ponty Mython?
    <BLANKLINE>

Test case #3: A test case with a short text and characters for 6 new lines

    >>> text_indentation("Hello world. Monty Python? It's is:")
    Hello world.
    <BLANKLINE>
    Monty Python?
    <BLANKLINE>
    It's is:
    <BLANKLINE>

Test case #4: A test case with a text with a special format

    >>> text_indentation("""Bye world. \
    ... Python Monty? \
    ... Isn't""")
    Bye world.
    <BLANKLINE>
    Python Monty?
    <BLANKLINE>
    Isn't

Test case #5: A test case with only spaces and characters to prints newlines

    >>> text_indentation("   ?:.   ")
    ?
    <BLANKLINE>
    :
    <BLANKLINE>
    .
    <BLANKLINE>

Test case #6: Another test case with only spaces and characters to prints newlines

    >>> text_indentation("  .??:?.  ")
    .
    <BLANKLINE>
    ?
    <BLANKLINE>
    ?
    <BLANKLINE>
    :
    <BLANKLINE>
    ?
    <BLANKLINE>
    .
    <BLANKLINE>

Section // Incorrect Parameters
===============================

Test case #7: A test case with an integer parameter

    >>> text_indentation(15)
    Traceback (most recent call last):
    TypeError: text must be a string

Test case #8: A test case with an boolean parameter

    >>> text_indentation(True)
    Traceback (most recent call last):
    TypeError: text must be a string

Test case #9: A test case with a data type parameter

    >>> text_indentation(str)
    Traceback (most recent call last):
    TypeError: text must be a string

Test case #10: A test case with an infinite float number

    >>> text_indentation(1e400)
    Traceback (most recent call last):
    TypeError: text must be a string
