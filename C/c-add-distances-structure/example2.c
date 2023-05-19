#include <stdio.h>
#include <math.h>

struct Distance
{
    float feet;
    float inch;
} firstDistance, secondDistance, sum;

int main()
{
    printf("Enter feet and inch for the first distance with a space : \n");
    scanf("%f %f", &firstDistance.feet, &firstDistance.inch);

    printf("Enter feet and inch for the second distance with a space : \n");
    scanf("%f %f", &secondDistance.feet, &secondDistance.inch);

    sum.feet = firstDistance.feet + secondDistance.feet;
    sum.inch = firstDistance.inch + secondDistance.inch;

    if (sum.inch >= 12)
    {
        sum.feet += (int)(sum.inch / 12);
        sum.inch = fmod(sum.inch, 12);
    }

    printf("Sum is %.1f feet, %.1f inches\n", sum.feet, sum.inch);
    return 0;
}