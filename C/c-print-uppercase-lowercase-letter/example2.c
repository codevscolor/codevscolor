// https://codevscolor.com/c-print-uppercase-lowercase-letter
#include <stdio.h>

int main()
{
    char ch = 'A';

    printf("Uppercase characters:\n");

    while (ch <= 'Z')
    {
        printf("%c ", ch);
        ch++;
    }

    ch = 'a';
    printf("\nLowercase characters:\n");
    while (ch <= 'z')
    {
        printf("%c ", ch);
        ch++;
    }

    return 0;
}