#include "menger.h"
/**
 * menger - function to creat a menger
 * @level: is the depth of the menger
 * Return: Nothing
 */
void menger(int level)
{
	int size, i, j, x, y, flag;

	size = pow(3, level);

	for (i = 0; i < size; i++)
	{
		for (j = 0; j < size; j++)
		{
			x = i;
			y = j;
			flag = 0;
			while (x >= 1 || y >= 1)
			{
				if (x % 3 == 1 && y % 3 == 1)
				{
					flag = 1;
					printf(" ");
					break;
				}
				x = x / 3;
				y = y / 3;
			}
			/* we print in that way because it is different*/
			/* than printf(#) */
			if (flag == 0)
				printf("%c", '#');
		}
		printf("\n");
	}
}