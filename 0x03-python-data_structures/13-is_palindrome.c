#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
  * is_palindrome - Checks if a singly linked list is a palindrome
  * @head: The head of the singly linked list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
    listint_t *current = NULL;
    int stat = 0;
    char *buffer = NULL;

    if (head == NULL)
        return (stat);
    
    if (*head == NULL)
        return (1);
    
    current = *head;

    while (current != NULL)
    {
        buffer = malloc(sizeof(char) * 500);
        if (buffer == NULL)
            return (0);

        sprintf(buffer, "%d", current->n);
        stat = str_is_palindrome(buffer);
        free(buffer);
        current = current->next;
    }

    return (stat);
}

/**
  * str_is_palindrome - Checks if a string is a palindrome
  * @str: The string to checks
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int str_is_palindrome(char *str)
{
    unsigned int i = 0, stat = 1, len_cyc = 0, len_str = 0;

    len_str = strlen(str) - 1;
    len_cyc = strlen(str) / 2;

    for (; i < len_cyc; ++i)
    {
        if (str[i] != str[len_str])
        {
            stat = 0;
            break;
        }

        --len_str;
    }

    return (stat);
}