using System;
using System.IO;
using Interfaces;
using Serilog.Core;

namespace Day01
{
    public class Solution1 : ISolution
    {
        private int totalFuel = 0;

        public int TotalFuel {
            get { return totalFuel; }
        }

        /// <summary>
        /// Calculates the required fuel for each module and adds it to totalFuel.
        /// </summary>
        /// <param name="mass">The mass of each fuel module.</param>
        public void RequiredFuel(int mass)
        {
            int fuel = mass / 3 - 2;
            totalFuel += fuel;
        }

        public static void Run(string filePath, Logger log)
        {
            Solution1 solution = new Solution1();

            foreach(string line in File.ReadLines(filePath))
            {
                int mass = Int32.Parse(line);
                solution.RequiredFuel(mass);
            }

            log.Information($"Total fuel required: {solution.totalFuel}");
        }
    }
}