// https://codevscolor.com/c-remainder-without-modulo-operator
#include <stdio.h>

int getRemainder(int no, int divisor)
{
    int multiplier = 1;
    int product = 0;

    while (product <= no)
    {
        product = divisor * multiplier;
        multiplier++;
    }

    return no - (product - divisor);
}

int main()
{
    int no, divisor, remainder;

    printf("Enter the number: ");
    scanf("%d", &no);

    printf("Enter the divisor: ");
    scanf("%d", &divisor);

    remainder = getRemainder(no, divisor);

    printf("The remainder is %d", remainder);

    return 0;
}