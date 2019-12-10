#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *turtle = NULL, *hare = NULL;
	int found = 0;

	if (list)
	{
		turtle = list;
		hare = list->next;
		while (turtle)
		{
			if (!hare->next)
				break;
			
			if (!hare->next->next)
				break;

			if (turtle == hare)
			{
				found = 1;
				break;
			}

			turtle = list->next;
			hare = hare->next->next;
		}
	}

	return (found);
}
