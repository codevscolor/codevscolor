// https://codevscolor.com/c-plus-plus-print-data-table

#include <iostream>
#include <iomanip>

using namespace std;

class Student
{
public:
    string studentName;
    int studentAge;
    int studentMarks;
    int admissionYear;

    Student(string name, int age, int marks, int year)
    {
        studentName = name;
        studentAge = age;
        studentMarks = marks;
        admissionYear = year;
    }
};

int main()
{
    Student studentArray[4] = {Student("Alex", 20, 80, 2018), Student("Bob", 21, 82, 2018), Student("Chandler", 23, 85, 2017), Student("Rose", 18, 89, 2019)};

    cout
        << left
        << setw(10)
        << "Name"
        << left
        << setw(5)
        << "Age"
        << left
        << setw(8)
        << "Marks"
        << left
        << setw(5)
        << "Year"
        << endl;

    for (int i = 0; i < 4; i++)
    {
        cout
            << left
            << setw(10)
            << studentArray[i].studentName
            << left
            << setw(5)
            << studentArray[i].studentAge
            << left
            << setw(8)
            << studentArray[i].studentMarks
            << left
            << setw(5)
            << studentArray[i].admissionYear
            << endl;
    }
    return 0;
}