// https://codevscolor.com/c-plus-plus-print-data-table

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout
        << setfill('*')
        << left
        << setw(5)
        << "one" << endl;

    return 0;
}