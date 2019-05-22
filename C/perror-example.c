#include <stdio.h>
#include <errno.h>
int main()
{
    //1
    perror("error found");
    printf("errno = %d\n", errno);
    FILE *f;
    //2
    if ((f = fopen("file.txt", "r")) == NULL)
    {
        //3
        perror("Error opening the file");
        printf("errno = %d\n", errno);
    }
    //4
    perror("error found");
    printf("errno = %d\n", errno);
}
