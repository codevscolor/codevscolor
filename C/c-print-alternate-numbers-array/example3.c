// https://codevscolor.com/c-print-alternate-numbers-array
#include <stdio.h>

int main()
{
    int i;
    int size;

    printf("How many numbers you want to enter: ");
    scanf("%d", &size);

    if (size <= 0)
    {
        printf("Please enter a valid input!!");
        return 0;
    }
    int array[size];

    i = 0;
    do
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &array[i]);
        i++;
    } while (i < size);

    printf("Alternate elements of the input array: \n");
    i = 0;
    do
    {
        printf("%d ", array[i]);
        i += 2;
    } while (i < size);
}