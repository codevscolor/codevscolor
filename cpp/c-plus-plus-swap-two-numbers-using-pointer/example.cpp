// https://codevscolor.com/c-plus-plus-swap-two-numbers-using-pointer
#include <iostream>
using namespace std;

void swap(int *first, int *second)
{
    int temp;

    temp = *first;
    *first = *second;
    *second = temp;
}

int main()
{
    int a, b;

    cout << "Enter the numbers : " << endl;
    cin >> a;
    cin >> b;

    cout << "Before swap, a = " << a << ", b = " << b << endl;
    swap(&a, &b);
    cout << "After swap, a = " << a << ", b = " << b << endl;
}