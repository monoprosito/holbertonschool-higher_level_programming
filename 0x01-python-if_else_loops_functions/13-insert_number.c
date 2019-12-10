#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to inserts in the singly linked list
  *
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *new_node = NULL, *temp = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (*head)
	{
		current = *head;
		if (number <= current->n)
		{
			new_node->next = current;
			*head = new_node;
		}
		else
		{
			while (current->next)
			{
				if (number <= current->next->n)
				{
					temp = current->next;
					current->next = new_node;
					new_node->next = temp;
					return (*head);
				}

				current = current->next;
			}
			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (*head);
}
