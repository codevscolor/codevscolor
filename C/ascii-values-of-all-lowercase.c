#include <stdio.h>
int main()
{
    //1
    int start = 'a';
    //2
    while (start <= 'z')
    {
        //3
        printf("%c : %d\n", start, start);
        //4
        start++;
    }
    return 0;
}
