// https://codevscolor.com/c-program-separate-even-odd-numbers-array
#include <stdio.h>

int main()
{
    int i, j, k;

    int num[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int odd[10];
    int even[10];

    j = 0;
    k = 0;

    for (i = 0; i < 10; i++)
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

    printf("Even numbers : ");
    for (i = 0; i < j; i++)
    {
        printf("%d ", even[i]);
    }

    printf("\nOdd numbers : ");
    for (i = 0; i < k; i++)
    {
        printf("%d ", even[i]);
    }

    printf("\n");
    return 0;
}
