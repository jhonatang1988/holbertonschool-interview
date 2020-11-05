#include "binary_trees.h"

/**
 * AVL_tree - function that builds an AVL tree from an array helper
 * @array: array
 * @begin: first index
 * @last: last index
 * Return: new node or NULL otherwise
 */
avl_t *AVL_tree(int *array, int begin, int last)
{
	avl_t *node, *left, *right;
	int mid;


	if (begin > last)
		return (NULL);

	mid = (last + begin) / 2;
	left = AVL_tree(array, begin, mid - 1);
	right = AVL_tree(array, mid + 1, last);

	node = malloc(sizeof(avl_t));
	if (!node)
		return (NULL);
	node->n = array[mid];
	node->parent = NULL;
	node->left = left;
	node->right = right;

	if (left != NULL)
		left->parent = node;
	if (right != NULL)
		right->parent = node;

	return (node);
}

/**
 * sorted_array_to_avl - main
 * @array: array
 * @size: size
 * Return: tree or NULL otherwise
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	if (array == NULL)
		return (NULL);
	return (AVL_tree(array, 0, (int)(size - 1)));
}