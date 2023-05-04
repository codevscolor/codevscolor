// https://codevscolor.com/c-plus-plus-find-factorial-class

#include <iostream>
using namespace std;

class Factorial
{
public:
    static unsigned long long calculateFactorial(unsigned long long num)
    {
        if (num == 0 || num == 1)
        {
            return 1;
        }
        return num * calculateFactorial(num - 1);
    }
};

int main()
{
    int num;

    cout << "Enter a number :" << endl;
    cin >> num;

    unsigned long long factorial = Factorial::calculateFactorial(num);
    cout << "Factorial: " << factorial << endl;
}