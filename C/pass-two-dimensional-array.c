#include<stdio.h>
//7
void print(int m, int n, int arr[m][n])
{
    //8
    int i, j;
    //9
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d ", arr[i][j]);
        }
        //10
        printf("\n");
    }
    printf("\n");
}
int main()
{
    //1
    int rowCount, columnCount;
    int i, j;
    //2
    printf("Enter the row count : ");
    scanf("%d", &rowCount);
    //3
    printf("Enter the column count : ");
    scanf("%d", &columnCount);
    //4
    int array[rowCount][columnCount];
    //5
    for (i = 0; i < rowCount; i++)
    {
        for (j = 0; j < columnCount; j++)
        {
            printf("Enter value for array[%d][%d] : ", i, j);
            scanf("%d", &array[i][j]);
        }
    }
    //6
    print(rowCount, columnCount, array);
    return 0;
}
