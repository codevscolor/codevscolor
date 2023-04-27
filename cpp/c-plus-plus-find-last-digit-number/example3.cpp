// https://codevscolor.com/c-plus-plus-find-last-digit-number
#include <iostream>
using namespace std;

int main()
{
    int number;
    cout << "Enter a number : " << endl;
    cin >> number;

    string strNumber = to_string(number);
    int firstDigit = strNumber.front() - '0';
    int lastDigit = strNumber.back() - '0';

    cout << "First digit is : " << firstDigit << endl;
    cout << "Last digit is : " << lastDigit << endl;
    return 0;
}