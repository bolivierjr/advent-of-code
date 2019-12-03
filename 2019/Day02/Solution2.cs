using System;
using System.IO;
using Interfaces;
using Serilog.Core;

namespace Day02
{
    public class Solution2: ISolution
    {
        private const int target = 19690720;
        private int nounVerb;
        
        public void NounAndVerbGenerator(int[] memory)
        {
            for (int noun = 0; noun < 99; noun++)
            {
                for (int verb = 0; verb < 99; verb++)
                {
                    memory[1] = noun;
                    memory[2] = verb;

                    int[] processed = this.OptcodeProcessor(memory);

                    if(processed[0] == target)
                    {
                        nounVerb = 100 * noun + verb;
                    }
                }
            }
        }

        public int[] OptcodeProcessor(int[] memory)
        {
            var optcodes = new int[memory.Length];
            Array.Copy(memory, optcodes, memory.Length);

            for (int index = 0; index < optcodes.Length; index += 4)
            {
                if (optcodes[index] == 99) break;
                
                if (optcodes[index] == 1)
                {
                    int sum = optcodes[optcodes[index + 1]] + optcodes[optcodes[index + 2]];
                    // Change output position value
                    optcodes[optcodes[index + 3]] = sum;

                }
                else if (optcodes[index] == 2)
                {
                    int product = optcodes[optcodes[index + 1]] * optcodes[optcodes[index + 2]];
                    // Change output position value
                    optcodes[optcodes[index + 3]] = product;
                }
            }

            return optcodes;
        }

        public static void Run(string filePath, Logger log)
        {
            string intcodeProgram = File.ReadAllText(filePath);
            string[] optcodes = intcodeProgram.Split(",");
            int[] optcodeNums = Array.ConvertAll<string,int>(optcodes, int.Parse);

            Solution2 solution = new Solution2();
            solution.NounAndVerbGenerator(optcodeNums);

            log.Information($"Answer is {solution.nounVerb}");
        }
    }
}