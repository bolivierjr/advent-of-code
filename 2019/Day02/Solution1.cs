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
            for (int index = 0; index < optcodes.Length; index += 4)
            {
                // Put the next opcodes in place.
                int operation = optcodes[index];
                int inputOne = optcodes[index + 1];
                int inputTwo = optcodes[index + 2];
                int output = optcodes[index + 3];

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
            }

            int result = optcodes[0];

            return result;
        }

        public static void Run(string filePath, Logger log)
        {
            string intcodeProgram = File.ReadAllText(filePath);
            string[] optcodes = intcodeProgram.Split(",");
            int[] optcodeNums = Array.ConvertAll<string, int>(optcodes, int.Parse);

            // 1202 program alarm state
            optcodeNums[1] = 12;
            optcodeNums[2] = 2;

            Solution1 solution = new Solution1();
            int processed = solution.OptcodeProcessor(optcodeNums);

            log.Information($"Answer is {processed}");
        }
    }
}
