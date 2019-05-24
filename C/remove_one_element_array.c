    #include <stdio.h>
    #include <stdlib.h>
    int main()
    {
        //1
        int *array, size, elementToDelete, i, position;
        //2
        printf("Enter total number of elements to add : ");
        scanf("%d", &size);
        array = (int *)malloc(size * sizeof(int));
        //3
        for (i = 0; i < size; i++)
        {
            printf("Enter element for position %d : ", i);
            scanf("%d", &array[i]);
        }
        //4
        printf("You have entered : ");
        for (i = 0; i < size; i++)
        {
            printf("%d ", array[i]);
        }
        printf("\n");
        //5
        printf("Enter the number you want to delete : ");
        scanf("%d", &elementToDelete);
        //6
        position = -1;
        //7
        for (i = 0; i < size; i++)
        {
            if (array[i] == elementToDelete)
            {
                position = i;
                break;
            }
        }
        //8
        if (position != -1)
        {
            //9
            for (i = position; i < size - 1; i++)
            {
                array[i] = array[i + 1];
            }
            array = (int *)realloc(array, (size - 1) * sizeof(int));
            //10
            printf("Final array :");
            for (i = 0; i < size - 1; i++)
            {
                printf("%d ", array[i]);
            }
            printf("\n");
        }
        else
        {
            //11
            printf("Entered number is not found in the array.");
        }
    }
