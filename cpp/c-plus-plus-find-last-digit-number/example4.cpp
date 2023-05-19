// https://codevscolor.com/c-plus-plus-find-last-digit-number
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int number;
    cout << "Enter a number : " << endl;
    cin >> number;

    cout << "Last digit is : " << number % 10 << endl;

    int d = (int)log10(number);
    int firstDigit = (int)(number / pow(10, d));

    cout << "First digit is : " << firstDigit << endl;
    return 0;
}