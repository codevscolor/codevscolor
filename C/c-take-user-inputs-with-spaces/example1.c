// https://codevscolor.com/c-take-user-inputs-with-spaces

#include<stdio.h>

int main()
{
    char input[30];
    printf("Enter a string: ");
    scanf("%[^\n]", input);

    printf("You have entered: %s\n", input);
    return 0;
}