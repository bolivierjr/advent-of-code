using System;
using System.Linq;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;
using Utils;

namespace Day04
{
    public class Solution1 : ISolution
    {
        public bool IfDecrease(int[] pass)
        {
            var neverDecrease = false;
            for (var index = 0; index < 5; index++)
            {
                if (pass[index] <= pass[index + 1])
                {
                    neverDecrease = true;
                }
                else
                {
                    neverDecrease = false;
                    break;
                }
            }
            return neverDecrease;
        }

        public bool IfDupilcate(int[] pass)
        {
            var duplicate = false;
            Dictionary<int, int> intCount = Counter.CountInt(pass);

            foreach (KeyValuePair<int, int> integer in intCount)
            {
                if (integer.Value >= 2)
                    duplicate = true;
            }
            return duplicate;
        }

        public int FindPasswords(string[] range)
        {
            var rangeInt = Array.ConvertAll(range, int.Parse);
            var passwords = new List<int>();
            for (int pass = rangeInt[0]; pass <= rangeInt[1]; pass++)
            {
                var passToCharArray = pass.ToString().ToCharArray();
                var passToIntArray = Array.ConvertAll(
                    passToCharArray, x => (int)Char.GetNumericValue(x));
                Console.WriteLine(pass);
                if (IfDecrease(passToIntArray) && IfDupilcate(passToIntArray))
                {
                    passwords.Add(pass);
                }
            }
            return passwords.Count;
        }
        public static void Run(string filePath, Logger log)
        {
            var input = "240298-784956".Split("-");

            var sol = new Solution1();
            int passwords = sol.FindPasswords(input);
            log.Information($"Amount of passwords is: {passwords}");
        }
    }
}
