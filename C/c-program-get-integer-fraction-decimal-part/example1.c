// https://codevscolor.com/c-program-get-integer-fraction-decimal-part

#include <stdio.h>

int main()
{
    float num;

    printf("Enter a number: ");
    scanf("%f", &num);

    int num_integer = (int)num;
    float num_decimal = num - num_integer;

    printf("Integer part: %d, Decimal part: %f\n", num_integer, num_decimal);

    return 0;
}