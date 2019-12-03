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
            int[] memory = (int[])optcodes.Clone();

            for (int noun = 0; noun < 100; noun++)
            {
                for (int verb = 0; verb < 100; verb++)
                {
                    memory[1] = noun;
                    memory[2] = verb;

                    this.OptcodeProcessor(memory);

                    if(memory[0] == 19690720)
                    {
                        return 1;
                    }
                }
            }

            return 0;
        }

        public void OptcodeProcessor(int[] optcodes)
        {

            for (int index = 0; index < optcodes.Length; index += 4)
            {
                if (optcodes[index] == 99)
                {
                    break;
                }
                
                else if (optcodes[index] == 1)
                {
                    int sum = optcodes[index + 1] + optcodes[index + 2];
                    // Change output position value
                    optcodes[index + 3] = sum;

                }
                else if (optcodes[index] == 2)
                {
                    int product = optcodes[index + 1] * optcodes[index + 2];
                    // Change output position value
                    optcodes[index + 3] = product;
                }
            }
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