// https://codevscolor.com/c-print-uppercase-lowercase-letter
#include <stdio.h>

int main()
{
    char ch = 'A';

    printf("Uppercase characters:\n");

    do
    {
        printf("%c ", ch);
        ch++;
    } while (ch <= 'Z');

    ch = 'a';
    printf("\nLowercase characters:\n");
    do
    {
        printf("%c ", ch);
        ch++;
    } while (ch <= 'z');

    return 0;
}