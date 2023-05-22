// https://codevscolor.com/c-program-separate-even-odd-numbers-array
#include <stdio.h>

void printArray(int arr[], int length){
    for(int i = 0; i < length; i++){
        printf("%d ", arr[i]);
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

    for(i = 0; i < size; i++){
        printf("Enter the number for position %d: ", i);
        scanf("%d", &num[i]);
    }

    j = 0;
    k = 0;

    for (i = 0; i < size; i++)
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
    }

    printf("Even numbers: ");
    printArray(even, j);

    printf("\nOdd numbers: ");
    printArray(odd, k);

    printf("\n");
    return 0;
}
