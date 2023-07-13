// https://codevscolor.com/c-plus-plus-check-alphanumeric-character

#include <iostream>
using namespace std;

int main()
{
    char str[100];
    bool isAllAlphanumeric = true;

    cout << "Enter a string to test:" << endl;
    cin.get(str, 100);

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (!isalnum(str[i]))
        {
            isAllAlphanumeric = false;
            break;
        }
    }

    if (isAllAlphanumeric)
    {
        cout << "The string contains only alphanumeric characters" << endl;
    }
    else
    {
        cout << "The string doesn't contain only alphanumeric character" << endl;
    }
}