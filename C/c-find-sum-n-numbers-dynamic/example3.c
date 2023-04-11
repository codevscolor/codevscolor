// https://codevscolor.com/c-find-sum-n-numbers-dynamic
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i = 0;
	int count;
	int *arr;
	int sum = 0;

	printf("Enter the total number of elements you want to enter : ");
	scanf("%d", &count);

	arr = (int *)malloc(count * sizeof(int));

	do
	{
		printf("Enter element %d : ", (i + 1));
		scanf("%d", arr + i);

		sum += *(arr + i);
		i++;
	} while (i < count);

	printf("sum is %d \n", sum);

	free(arr);
	return 0;
}