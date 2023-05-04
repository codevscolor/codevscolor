// https://codevscolor.com/c-read-numbers-file-store-array
#include <stdio.h>

int main(void)
{
    int numbers[50];
    int i = 0;
    FILE *file;

    if (file = fopen("testfile.txt", "r"))
    {
        while (fscanf(file, "%d", &numbers[i]) != EOF)
        {
            i++;
        }
        fclose(file);

        numbers[i] = '\0';

        for (i = 0; numbers[i] != '\0'; i++)
            printf("%d\n", numbers[i]);
    }

    return 0;
}