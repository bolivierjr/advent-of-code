using System;
using System.Linq;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;
using Utils;

namespace Day04
{
    public class Solution2 : Solution1, ISolution
    {
        public bool IfDouble(int[] pass)
        {
            var duplicate = false;
            Dictionary<int, int> intCount = Counter.CountInt(pass);

            foreach (KeyValuePair<int, int> integer in intCount)
            {
                if (integer.Value == 2)
                    duplicate = true;
            }
            return duplicate;
        }

        new public int FindPasswords(string[] range)
        {
            var rangeInt = Array.ConvertAll(range, int.Parse);
            var passwords = new List<int>();
            for (int pass = rangeInt[0]; pass <= rangeInt[1]; pass++)
            {
                var passToCharArray = pass.ToString().ToCharArray();
                var passToIntArray = Array.ConvertAll(
                    passToCharArray, x => (int)Char.GetNumericValue(x));

                if (IfDecrease(passToIntArray) && IfDouble(passToIntArray))
                {
                    passwords.Add(pass);
                }
            }
            return passwords.Count;
        }

        new public static void Run(string filePath, Logger log)
        {
            var input = "444555-444556".Split("-");

            var sol = new Solution2();
            int passwords = sol.FindPasswords(input);
            log.Information($"Amount of passwords is: {passwords}");
        }
    }
}
