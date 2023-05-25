// https://codevscolor.com/c-plus-plus-sum-digits-string

#include <iostream>

using namespace std;

int findSum(string str)
{
    int sum = 0;

    for (char ch : str)
    {
        if (ch >= '0' && ch <= '9')
        {
            sum += ch - '0';
        }
    }
    return sum;
}

int main()
{
    string str;
    cout << "Enter a string:" << endl;

    getline(cin, str);
    cout << "Sum: " << findSum(str) << endl;
}