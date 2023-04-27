// https://codevscolor.com/c-plus-plus-find-last-digit-number
#include <iostream>
using namespace std;

int main()
{
    int number;
    cout << "Enter a number : " << endl;
    cin >> number;

    cout << "Last digit is : " << number % 10 << endl;

    for (; number >= 10; number /= 10)
    {
    }

    cout << "First digit is : " << number << endl;
    return 0;
}