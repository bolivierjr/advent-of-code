using System;
using System.IO;
using Interfaces;
using Serilog.Core;

namespace Day03
{
    public class Solution2 : ISolution
    {
        public static void Run(string filePath, Logger log)
        {
            var solution2 = new Solution2();

            foreach(string line in File.ReadLines(filePath))
            {
                
            }

            log.Information($"Answer is: {1}");
        }
    }
}