#include "lists.h"

/**
 * insert_node - insert a new node depending of the value of the node
 * this have to respect the sort order
 * @head: pointer to list
 * @number: value of the new node
 * Return: the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *new;

	if (!head)
	{
		return (NULL);
	}

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	else
	{
		aux = *head;
		if (aux->n > new->n)
		{
			new->next = aux;
			*head = new;
			return (*head);
		}
		else
		{
			while (aux->next && (aux->next->n < new->n))
			{
				aux = aux->next;
			}
			new->next = aux->next;
			aux->next = new;
			return (new);
		}
	}
}