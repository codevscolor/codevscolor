using System;
namespace dotnet_sample
{
    class Program
    {
        static void Main(string[] args)
        {
            //1
            int n;
            //2
            Console.WriteLine("Enter a number : ");
            //3
            n = int.Parse(Console.ReadLine());
            //4
            if(n == 0)
            {
                Console.WriteLine(n + " is zero.");
            }
            else if(n > 0)
            {
                //5
                Console.WriteLine(n + " is a positive number.");
            }
            else
            {
                //6
                Console.WriteLine(n + " is a negative number.");
            }
        }
    }
}
