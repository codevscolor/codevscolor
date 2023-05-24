// https://codevscolor.com/c-sharp-find-maximum-occurring-character-in-string

using System;
namespace Main
{
    public class Example
    {

        private static char getMaxOccurrenceCharacter(String str)
        {
            int[] countArray = new int[256];
            int maxValue = 0;
            char resultChar = '\0';

            for (int i = 0; i < str.Length; i++)
            {
                countArray[str[i]]++;

                if (countArray[str[i]] > maxValue)
                {
                    maxValue = countArray[str[i]];
                    resultChar = str[i];
                }
            }

            return resultChar;
        }

        public static void Main()
        {
            Console.WriteLine("Enter a string :");
            String givenStr = Console.ReadLine();

            Console.WriteLine("The character with maximum occurrence is : " + getMaxOccurrenceCharacter(givenStr));

        }
    }
}