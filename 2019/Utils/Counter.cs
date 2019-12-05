using System;
using System.Collections.Generic;

namespace Utils
{
    public class Counter
    {
        public static Dictionary<string, int> CountChars(string message)
        {
            var counted = new Dictionary<string, int>();

            foreach (char letter in message)
            {
                var charToString = letter.ToString();
                if (counted.ContainsKey(charToString))
                {
                    counted[charToString]++;
                }
                else
                {
                    counted[charToString] = 1;
                }
            }

            return counted;
        }

        public static Dictionary<int, int> CountInt(int[] numbers)
        {
            var counted = new Dictionary<int, int>();

            foreach (int num in numbers)
            {
                if (counted.ContainsKey(num))
                {
                    counted[num]++;
                }
                else
                {
                    counted[num] = 1;
                }
            }

            return counted;
        }
    }
}
