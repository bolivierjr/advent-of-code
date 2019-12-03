using System;
using System.IO;
using Interfaces;
using Serilog.Core;

namespace Day02
{
    public class Solution1 : ISolution
    {
        public int OptcodeProcessor(int[] optcodes)
        {
            int operation = optcodes[0];
            int inputOne = optcodes[1];
            int inputTwo = optcodes[2];
            int output = optcodes[3];

            for (int index = 0; index < optcodes.Length; index+=4)
            {
                if (operation == 99)
                {
                    break;
                }
                else if (operation == 1)
                {
                    int sum = optcodes[inputOne] + optcodes[inputTwo];
                    // Change output position value
                    optcodes[output] = sum;

                }
                else if (operation == 2)
                {
                    int product = optcodes[inputOne] * optcodes[inputTwo];
                    // Change output position value
                    optcodes[output] = product;
                }

                if (index + 4 >= optcodes.Length) break;

                // Put the next four optcodes in place
                operation = optcodes[index];
                inputOne = optcodes[index + 1];
                inputTwo = optcodes[index + 2];
                output = optcodes[index + 3];
            }

            int result = optcodes[0];

            return result;
        }

        public static void Run(string filePath, Logger log)
        {
            string intcodeProgram = File.ReadAllText(filePath);
            string[] optcodes = intcodeProgram.Split(",");
            int[] optcodeNums = Array.ConvertAll<string,int>(optcodes, int.Parse);

            // 1202 program alarm state
            optcodeNums[1] = 12;
            optcodeNums[2] = 2;

            Solution1 solution = new Solution1();
            int processed = solution.OptcodeProcessor(optcodeNums);

            log.Information($"Answer is {processed}");
        }
    }
}