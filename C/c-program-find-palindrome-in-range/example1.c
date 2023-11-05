// https://codevscolor.com/c-program-find-palindrome-in-range

#include <stdio.h>

int main()
{
    int startNumber;
    int endNumber;
    int i;
    int currentNumber;
    int reversedNumber;
    int rem;

    printf("Enter the first number:");
    scanf("%d", &startNumber);

    printf("Enter the second number:");
    scanf("%d", &endNumber);

    printf("Palindrome number between %d and %d are:\n", startNumber, endNumber);

    for (i = startNumber; i <= endNumber; i++)
    {
        currentNumber = i;
        reversedNumber = 0;

        while (currentNumber)
        {
            rem = currentNumber % 10;
            currentNumber = currentNumber / 10;
            reversedNumber = reversedNumber * 10 + rem;
        }

        if(i == reversedNumber){
            printf("%d ", i);
        }
    }
    return 0;
}