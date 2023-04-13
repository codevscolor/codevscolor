#include <stdio.h>
#include <math.h>

int main()
{
	double num, integerValue, decimalValue;

	printf("Enter a number: ");
	scanf("%lf", &num);

	decimalValue = modf(num, &integerValue);

	printf("Integer part: %lf, Decimal part: %lf\n", integerValue, decimalValue);

	return 0;
}