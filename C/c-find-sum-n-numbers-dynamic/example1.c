// https://codevscolor.com/c-find-sum-n-numbers-dynamic
#include <stdio.h>
#include <stdlib.h>

int main()
{
	// 1
	int i;
	int count;
	int *arr;
	int sum = 0;

	// 2
	printf("Enter the total number of elements you want to enter : ");
	scanf("%d", &count);

	// 3
	arr = (int *)malloc(count * sizeof(int));

	// 4
	for (i = 0; i < count; i++)
	{
		// 5
		printf("Enter element %d : ", (i + 1));
		scanf("%d", arr + i);

		// 6
		sum += *(arr + i);
	}

	// 7
	printf("sum is %d \n", sum);

	// 8
	free(arr);
	return 0;
}