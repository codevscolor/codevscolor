// https://codevscolor.com/c-remainder-without-modulo-operator
#include <stdio.h>

int main()
{
    int no, divisor, remainder;

    printf("Enter the number : ");
    scanf("%d", &no);

    printf("Enter the divisor : ");
    scanf("%d", &divisor);

    while (no >= divisor)
    {
        no = no - divisor;
    }

    remainder = no;

    printf("The remainder is %d ", remainder);

    return 0;
}