#include <stdio.h>
int main()
{
    //1
    int oddCount = 0;
    int evenCount = 0;
    int sizeOfArray;
    int i;
    //2
    printf("Enter the size of the array : ");
    scanf("%d", &sizeOfArray);
    //3
    int array[sizeOfArray];
    //4
    for (i = 0; i < sizeOfArray; i++)
    {
        printf("Enter item for position %d : ", i);
        scanf("%d", &array[i]);
    }
    //5
    for (i = 0; i < sizeOfArray; i++)
    {
        //6
        if (array[i] % 2 == 0)
        {
            evenCount++;
        }
        else
        {
            oddCount++;
        }
    }
    //7
    printf("Even count : %d\n", evenCount);
    printf("Odd count : %d\n", oddCount);
    return 0;
}
