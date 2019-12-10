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
	listint_t *turtle = list, *hare = list;
	int found = 0;

	while ((turtle && hare) && hare->next)
	{		
		turtle = turtle->next;

		if (hare->next || hare->next->next)	
			hare = hare->next->next;
		else
			break;

		if (turtle == hare)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
