// https://codevscolor.com/c-print-alternate-numbers-array
#include <stdio.h>

int main()
{
    int i;
    int size;

    printf("How many numbers you want to enter: ");
    scanf("%d", &size);

    int array[size];

    for (i = 0; i < size; i++)
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    printf("Alternate elements of the input array: \n");
    for (i = 0; i < size; i += 2)
    {
        printf("%d ", array[i]);
    }
}