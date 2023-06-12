// https://codevscolor.com/c-program-read-print-string-word-new-line

#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

int main()
{
    char str[MAX_SIZE];

    printf("Enter a string: ");
    fgets(str, MAX_SIZE, stdin);

    int i;

    for (i = 0; i < strlen(str); i++)
    {
        if (str[i] == ' ' || i == strlen(str) - 1)
        {
            printf("\n");
        }
        else
        {
            printf("%c", str[i]);
        }
    }

    return 0;
}