// https://codevscolor.com/c-print-uppercase-lowercase-letter
#include <stdio.h>

int main()
{
    char ch;

    printf("Uppercase characters:\n");

    for (ch = 'A'; ch <= 'Z'; ch++)
    {
        printf("%c ", ch);
    }

    printf("\nLowercase characters:\n");
    for (ch = 'a'; ch <= 'z'; ch++)
    {
        printf("%c ", ch);
    }

    return 0;
}