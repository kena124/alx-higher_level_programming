#include "lists.h"

/**
 * is_palindrome - checks if a linked list
 * palindrome or not.
 * @head: pointer to the head of the linked list
 *
 * Return: 0 if it is not palindrome and
 * 1 if it is palindrome.
 */
int is_palindrome(listint_t **head)
{
	int len = 0, half_len = 0, count = 0;
	listint_t *cur, *prev;

	if (head == NULL || *head == NULL)
		return (1);
	cur = *head;
	prev = *head;

	if (cur->next == NULL)
		return (1);

	for (; cur != NULL; cur = cur->next, ++len)
		;
	half_len = len / 2;

	while ((cur = prev->next) && count < half_len - 1)
	{
		prev->next = cur->next;
		cur->next = *head;
		*head = cur;
		count++;
	}

	if (len % 2 != 0)
		cur = cur->next;

	for (prev = *head, count = 0; count < half_len && prev->n == cur->n;
	     prev = prev->next, cur = cur->next, count++)
		;

	if (cur == NULL)
		return (1);
	return (0);
}
