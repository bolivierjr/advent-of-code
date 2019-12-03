using System;
using System.IO;
using Interfaces;
using Serilog.Core;

namespace Day02
{
    public class Solution2: ISolution
    {
        public int NounAndVerbGenerator(int[] optcodes)
        {
            for (int noun = 0; noun < 100; noun++)
            {
                for (int verb = 0; verb < 100; verb++)
                {
                    optcodes[1] = noun;
                    optcodes[2] = verb;

                    bool processed = this.OptcodeProcessor(optcodes);

                    if(processed)
                    {
                        return 1;
                    }
                }
            }

            return 0;
        }

        public bool OptcodeProcessor(int[] optcodes)
        {
            int operation = optcodes[0];
            int inputOne = optcodes[1];
            int inputTwo = optcodes[2];
            int output = optcodes[3];

            for (int index = 0; index < optcodes.Length; index += 4)
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

                if (optcodes[0] == 19690720)
                {
                    return true;
                }

                if (index + 4 >= optcodes.Length) break;

                // Put the next four optcodes in place
                operation = optcodes[index];
                inputOne = optcodes[index + 1];
                inputTwo = optcodes[index + 2];
                output = optcodes[index + 3];
            }

            return false;
        }

        public static void Run(string filePath, Logger log)
        {
            string intcodeProgram = File.ReadAllText(filePath);
            string[] optcodes = intcodeProgram.Split(",");
            int[] optcodeNums = Array.ConvertAll<string,int>(optcodes, int.Parse);

            Solution2 solution = new Solution2();
            int processed = solution.NounAndVerbGenerator(optcodeNums);

            log.Information($"Answer is {processed}");
        }
    }
}