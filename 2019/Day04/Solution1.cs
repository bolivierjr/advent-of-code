using System;
using System.Linq;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;

namespace Day04
{
    public class Solution1 : ISolution
    {
        public bool IfDecreasing(int[] pass)
        {
            var neverDecrease = false;
            for (var index = 0; index < 5; index++)
            {
                if (pass[index] <= pass[index+1])
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

        public bool IfDuplicating(int[] pass)
        {
            var duplicate = false;
            for (var index = 0; index < 5; index++)
            {
                if (pass[index] == pass[index+1])
                    duplicate = true;
            }
            return duplicate;
        }

        public int FindPasswords(string[] range)
        {
            var rangeInt = Array.ConvertAll(range, int.Parse);
            var passwords = new List<int>();
            for (int pass = rangeInt[0]; pass < rangeInt[1]; pass++)
            {
                // Console.WriteLine(pass);
                var passToCharArray = pass.ToString().ToCharArray();
                var passToIntArray = Array.ConvertAll(
                    passToCharArray, x => (int)Char.GetNumericValue(x));

                if (IfDecreasing(passToIntArray) && IfDuplicating(passToIntArray))
                {
                    passwords.Add(pass);
                }
            }
            return passwords.Count;
        }
        public static void Run(string filePath, Logger log)
        {
            var input = "240298-784956";
            var inputList = input.Split("-");

            var sol = new Solution1();
            var passwords = sol.FindPasswords(inputList);
            log.Information($"Amount of passwords is: {passwords}");
        }
    }
}