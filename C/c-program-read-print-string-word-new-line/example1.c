// https://codevscolor.com/c-program-read-print-string-word-new-line

#include <stdio.h>
#include <string.h>

// 1
#define MAX_SIZE 100

int main()
{
    // 2
    char str[MAX_SIZE];

    // 3
    printf("Enter a string: ");
    fgets(str, MAX_SIZE, stdin);

    int i;
    int end;
    int start = 0;

    // 4
    for (i = 0; i < strlen(str); i++)
    {
        // 5
        if (str[i] == ' ' || i == strlen(str) - 1)
        {
            end = i;
            printf("%.*s\n", (end - start), str + start);
            start = i + 1;
        }
    }

    return 0;
}