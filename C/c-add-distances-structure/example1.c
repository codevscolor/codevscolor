#include <stdio.h>

struct Distance
{
    int feet;
    float inch;
} firstDistance, secondDistance, sum;

int main()
{
    printf("Enter feet and inch for the first distance with a space : \n");
    scanf("%d %f", &firstDistance.feet, &firstDistance.inch);

    printf("Enter feet and inch for the second distance with a space : \n");
    scanf("%d %f", &secondDistance.feet, &secondDistance.inch);

    sum.feet = firstDistance.feet + secondDistance.feet;
    sum.inch = firstDistance.inch + secondDistance.inch;

    while (sum.inch >= 12)
    {
        sum.inch = sum.inch - 12;
        sum.feet++;
    }

    printf("Sum is %d feet, %.1f inches\n", sum.feet, sum.inch);
    return 0;
}