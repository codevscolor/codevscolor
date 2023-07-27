// https://codevscolor.com/c-take-user-inputs-with-spaces

#include<stdio.h>

int main()
{
    char input[30], secondInput[30];
    
    printf("Enter a string: ");
    scanf("%[^\n]", input);

    getchar();

    printf("Enter another string: ");
    scanf("%[^\n]", secondInput);

    printf("First string: %s\n", input);
    printf("Second string: %s\n", secondInput);
    return 0;
}