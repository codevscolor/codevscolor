// https://codevscolor.com/c-plus-plus-print-odd-numbers
#include <iostream>
using namespace std;

int main()
{
    int i = 1;

    cout << "Using a for loop: " << endl;

    for (i = 1; i <= 100; i += 2)
    {
        cout << i << " ";
    }

    cout << "\n\nUsing a while loop: " << endl;

    i = 1;

    while (i <= 100)
    {
        cout << i << " ";
        i += 2;
    }

    cout << "\n\nUsing a do while loop: " << endl;

    i = 1;

    do
    {
        cout << i << " ";
        i += 2;
    } while (i <= 100);

    return 0;
}