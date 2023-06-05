// https://codevscolor.com/c-print-alternate-numbers-array
#include <stdio.h>

int main()
{
    int i;
    int size;

    printf("How many numbers you want to enter: ");
    scanf("%d", &size);

    int array[size];

    i = 0;
    while (i < size)
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &array[i]);
        i++;
    }

    printf("Alternate elements of the input array: \n");
    i = 0;
    while (i < size)
    {
        printf("%d ", array[i]);
        i += 2;
    }
}