using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;

namespace Day03
{
    public class Solution1 : ISolution
    {
        public List<Tuple<int,int>> GetStringLayout(string[] wirepath)
        {
            int xCoord = 0;
            int yCoord = 0;
            var coordinates = new List<Tuple<int,int>>();

            foreach(string wire in wirepath)
            {
                var letter = wire.Substring(0, 1);
                var number = wire.Substring(1);

                if (letter == "L")
                    xCoord = Int32.Parse($"-{number}");
                else if (letter == "R")
                    xCoord = Int32.Parse(number);

                if (letter == "U")
                {
                    yCoord = Int32.Parse(number);
                    coordinates.Add(Tuple.Create(xCoord, yCoord));
                }
                else if (letter == "D")
                {
                    yCoord = Int32.Parse($"-{number}");
                    coordinates.Add(Tuple.Create(xCoord, yCoord));
                }
            }

            return coordinates;
        }

        public static void Run(string filePath, Logger log)
        {

            var solution = new Solution1();
            var centralPort = new Tuple<int,int>(1,1);
            var coordList = new List<List<Tuple<int,int>>>();
            var lines = File.ReadLines(filePath, Encoding.UTF8);

            foreach (string line in lines)
            {
                var wirepath = line.Split(",");
                coordList.Add(solution.GetStringLayout(wirepath));
            }

            log.Information($"Answer is: {solution}");
        }
    }
}