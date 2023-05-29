// https://codevscolor.com/c-sharp-check-odd-even-number

namespace dotnet_sample
{
    class FirstExample
    {
        static void Main(string[] args)
        {
            int n;

            Console.WriteLine("Enter a number to check:");

            n = int.Parse(Console.ReadLine());

            if (n % 2 == 0)
            {
                Console.WriteLine(n + " is an even number");
            }
            else
            {
                Console.WriteLine(n + " is an odd number");
            }
        }
    }
}