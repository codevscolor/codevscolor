// https://codevscolor.com/c-plus-plus-print-odd-numbers
#include <iostream>
using namespace std;

int main()
{
    int i = 1;

    while (i <= 100)
    {
        if (i % 2 == 1)
        {
            cout << i << " ";
        }
        i++;
    }

    return 0;
}