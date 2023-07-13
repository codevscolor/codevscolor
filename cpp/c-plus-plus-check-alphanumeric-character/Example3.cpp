// https://codevscolor.com/c-plus-plus-check-alphanumeric-character

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string str;

    cout << "Enter a string to test:" << endl;
    getline(cin, str);

    bool isAllAlphanumeric = find_if(begin(str), end(str), ::isalnum) == str.end();

    if (isAllAlphanumeric)
    {
        cout << "The string contains only alphanumeric characters" << endl;
    }
    else
    {
        cout << "The string doesn't contain only alphanumeric character" << endl;
    }
}