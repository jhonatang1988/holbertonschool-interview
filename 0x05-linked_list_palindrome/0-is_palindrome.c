#include "lists.h"
/**
 * is_palindrome - function that says if a linked_list is palidrome or not
 * @head: pointer to the head of the linked_list
 * Return: 1 if the linked list is palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int count = 0, c, numbers[1000000];
	listint_t *aux;


	if (!(*head))
		return (1);
	aux = *head;
	while (aux != NULL)
	{
		numbers[count] = aux->n;
		aux = aux->next;
		count++;
	}
	count--;
	for (c = 0; c <= count / 2; c++)
	{
		if (numbers[c] != numbers[count - c])
			return (0);
	}
	return (1);
}