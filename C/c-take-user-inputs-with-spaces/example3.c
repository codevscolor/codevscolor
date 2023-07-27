// https://codevscolor.com/c-take-user-inputs-with-spaces

#include<stdio.h>

int main()
{
    char input[30], secondInput[30];
    
    printf("Enter a string: ");
    fgets(input, 30, stdin);

    printf("Enter another string: ");
    fgets(secondInput, 30, stdin);

    printf("First string: %s", input);
    printf("Second string: %s", secondInput);
    return 0;
}