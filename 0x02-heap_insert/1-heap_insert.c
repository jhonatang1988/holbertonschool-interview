#include "binary_trees.h"
/**
 * change - change two nodes in order to respect max heap order
 * @menor: leaf with smaller n
 * @mayor: leaf with bigger n
 * @n: 1 if the change was to be in left side or 2 in right side
 * @root: set the pointer to head in some circunstances
 * Return: the new updated node
 */
heap_t *change(heap_t *menor, heap_t *mayor, int n, heap_t **root)
{
	heap_t *aux = menor->parent, *r = menor->right, *l = menor->left;
	heap_t *r1 = mayor->right, *l1 = mayor->left;

	mayor->parent = aux;
	menor->parent = mayor;
	if (aux)
	{
		if (aux->left == menor)
			aux->left = mayor;
		if (aux->right == menor)
			aux->right = mayor;
	}
	if (mayor->left)
		mayor->left->parent = menor;
	if (mayor->right)
		mayor->right->parent = menor;
	if (n == 1)
	{
		mayor->right = r;
		mayor->left = menor;
		if (r)
			r->parent = mayor;
	}
	else
	{
		mayor->left = l;
		mayor->right = menor;
		if (l)
			l->parent = mayor;
	}
	menor->left = l1;
	menor->right = r1;
	if (!aux)
		*root = mayor;
	return (mayor);
}

/**
 * deep - return the deep of a binary tree
 * @tree: binary tree to go through
 * Return: 0 if it is already null or 1 or bigger of not
 */
int deep(heap_t *tree)
{
	int left = 1, right = 1, result;

	if (tree == NULL)
		return (0);
	left += deep(tree->left);
	right += deep(tree->right);
	if (right == left)
		result = left + 1;
	else
		result = right < left ? right : left;
	return (result);
}
/**
 * insert_order - insert the node without heap order, just
 * as complete binary tree, completing levels one by one
 * @head: actual leaf
 * @value: value to save
 * Return: the node in the binary tree
 */
heap_t *insert_order(heap_t *head, int value)
{
	int deepl, deepr;
	heap_t *new;

	deepl = deep(head->left);
	deepr = deep(head->right);
	if (deepl == 0 || deepr == 0)
	{
		new = malloc(sizeof(heap_t));
		if (!new)
			return (NULL);
		new->n = value;
		if (deepl == 0)
			head->left = new;
		else
			head->right = new;
		new->parent = head;
		new->left = NULL;
		new->right = NULL;
	}
	else if (deepl <= deepr && deepl != 0)
		new = insert_order(head->left, value);
	else if (deepl > deepr)
		new = insert_order(head->right, value);
	return (new);
}
/**
 * sort - sort the binary tree cuz it isnt sorted
 * @head: actual leaf
 * @root: pointer to the head of the binary tree
 * Return: the node updated or the original
 * if it respects the order of max heap
 */
heap_t *sort(heap_t *head, heap_t **root)
{
	heap_t *left, *right;

	if (head == NULL)
		return (head);
	left = sort(head->left, root);
	right = sort(head->right, root);
	if (!left && !right)
		return (head);
	if (left && left->n > head->n)
		return (change(head, head->left, 1, root));
	if (right && right->n > head->n)
		return (change(head, head->right, 2, root));
	return (head);
}
/**
 * heap_insert - Creating a max heap Binary tree
 * @root: pointer to head of binary tree
 * @value: number inside the heap
 * Return: return the node or NULL if it fails
 */
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *tree;

	if (*root == NULL)
	{
		tree = malloc(sizeof(heap_t));
		if (!tree)
			return (NULL);
		tree->parent = NULL;
		tree->n = value;
		tree->left = NULL;
		tree->right = NULL;
		*root = tree;
		return (tree);
	}
	tree = insert_order(*root, value);
	sort(*root, root);
	return (tree);
}