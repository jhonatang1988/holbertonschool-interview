#include "lists.h"
/**
 * checks if a singly linked list has a cycle in it
 * @list: linked list to go throught
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *rabbit, *turtle;


	if (!list)
		return (0);
	turtle = list;
	rabbit = list;
	/* with this form we verify all the positions
	  in a faster way*/
	while (rabbit && rabbit->next && rabbit->next->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (rabbit == turtle)
			return (1);
	}
	return (0);
}