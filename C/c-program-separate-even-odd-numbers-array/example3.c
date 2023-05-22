// https://codevscolor.com/c-program-separate-even-odd-numbers-array
#include <stdio.h>

void printArray(int arr[], int length)
{
    int i = 0;
    while (i < length)
    {
        printf("%d ", arr[i]);
        i++;
    }
}

int main()
{
    int i, j, k, size;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int num[size];
    int odd[size];
    int even[size];

    i = 0;
    while (i < size)
    {
        printf("Enter the number for position %d: ", i);
        scanf("%d", &num[i]);
        i++;
    }

    i = 0, j = 0, k = 0;

    while (i < size)
    {
        if (num[i] % 2 == 0)
        {
            even[j] = num[i];
            j++;
        }
        else
        {
            odd[k] = num[i];
            k++;
        }
        i++;
    }

    printf("Even numbers: ");
    printArray(even, j);

    printf("\nOdd numbers: ");
    printArray(odd, k);

    printf("\n");
    return 0;
}
