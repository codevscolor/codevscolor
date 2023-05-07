// https://codevscolor.com/c-remainder-without-modulo-operator
#include <stdio.h>

int getRemainder(int no, int divisor)
{
    return no - divisor * (no / divisor);
}

int main()
{
    int no, divisor, remainder;

    printf("Enter the number : ");
    scanf("%d", &no);

    printf("Enter the divisor : ");
    scanf("%d", &divisor);

    remainder = getRemainder(no, divisor);

    printf("The remainder is %d ", remainder);

    return 0;
}