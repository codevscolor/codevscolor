// https://codevscolor.com/c-plus-plus-print-even-numbers-one-hundred
#include <iostream>
using namespace std;

int main()
{
    int i = 2;
    do
    {
        cout << i << endl;
        i = i + 2;
    } while (i <= 100);

    return 0;
}