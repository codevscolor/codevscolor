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
            Console.WriteLine("Enter a number to check : ");
            //3
            n = int.Parse(Console.ReadLine());
            //4
            if(n % 2 == 0)
            {
              //5
                Console.WriteLine(n + " is an even number");
            }
            else
            {
              //6
                Console.WriteLine(n + " is an odd number");
            }
        }
    }
}
