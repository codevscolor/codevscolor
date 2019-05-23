#include <stdio.h>
int main()
{
    int oddCount = 0;
    int evenCount = 0;
    int sizeOfArray;
    int i;
    printf("Enter the size of the array : ");
    scanf("%d", &sizeOfArray);
    int array[sizeOfArray];
    while(i < sizeOfArray)
    {
        printf("Enter item for position %d : ", i);
        scanf("%d", &array[i]);
        i++;
    }
    i = 0;
    
    while(i < sizeOfArray)
    {
        if (array[i] % 2 == 0)
        {
            evenCount++;
        }
        else
        {
            oddCount++;
        }
        i++;
    }
    printf("Even count : %d\n", evenCount);
    printf("Odd count : %d\n", oddCount);
    return 0;
}
