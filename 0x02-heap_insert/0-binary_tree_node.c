#include "binary_trees.h"
/**
 * binary_tree_node - creates a binary tree
 *
 * @parent: parent node
 * @value: data
 *
 * Return: pointer of the new node or NULL if failure
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *tempNode = parent;
	binary_tree_t *newNode = NULL;

	if (!tempNode)
	{
		tempNode = malloc(sizeof(binary_tree_t));
		if (!tempNode)
			return (NULL);
		tempNode->n = value;
		tempNode->parent = NULL;
		tempNode->left = NULL;
		tempNode->right = NULL;
		return (tempNode);
	}
	else
	{
		newNode = malloc(sizeof(binary_tree_t));
		if (!newNode)
			return (NULL);

		newNode->parent = tempNode;
		newNode->n = value;
		newNode->left = NULL;
		newNode->right = NULL;

		if (tempNode->n > value)
		{
			tempNode->left = newNode;
		}
		else
		{
			tempNode->right = newNode;
		}
		return (newNode);
	}

}
