// https://codevscolor.com/c-sort-characters-string-ascii-values
#include <stdio.h>

int main()
{
    // 1
    int countArray[256];
    char inputString[100];
    int i, j;

    // 2
    printf("Enter a string : ");
    fgets(inputString, 100, stdin);

    // 3
    for (i = 0; i < 256; i++)
    {
        countArray[i] = 0;
    }

    // 4
    for (i = 0; inputString[i]; i++)
    {
        countArray[inputString[i]]++;
    }

    // 6
    printf("\nAfter sorting : ");

    // 7
    for (i = 0; i < 256; i++)
    {
        for (j = 0; j < countArray[i]; j++)
        {
            printf("%c", i);
        }
    }
}