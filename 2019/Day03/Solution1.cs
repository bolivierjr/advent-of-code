using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;

// ** WIP ** 
namespace Day03
{
    public class Solution1 : ISolution
    {
        public List<Tuple<int,int>> GetWireLayout(string[] wirepath)
        {
            int xCoord = 0;
            int yCoord = 0;
            var coordinates = new List<Tuple<int,int>>();

            foreach(string wire in wirepath)
            {
                var letter = wire.Substring(0, 1);
                var number = Int32.Parse(wire.Substring(1));
                for (var i = 0; i < number; i++)
                {
                    if (letter == "L") xCoord--;
                    else if (letter == "R") xCoord++;
                    else if (letter == "U") yCoord++;
                    else if (letter == "D") yCoord--;

                    coordinates.Add(Tuple.Create(xCoord, yCoord));
                }
            }

            return coordinates;
        }

        public HashSet<Tuple<int,int>> FindIntersections(
            List<Tuple<int,int>> wireOne, List<Tuple<int,int>> wireTwo)
        {       
            var wireOneSet = new HashSet<Tuple<int,int>>(wireOne);
            var wireTwoSet = new HashSet<Tuple<int,int>>(wireTwo);
            var intersections = new HashSet<Tuple<int,int>>(wireTwoSet);
            intersections.IntersectWith(wireOneSet);

            return intersections;
        }

        public int GetClosestDistance(HashSet<Tuple<int,int>> intersections)
        {
            var origin = Tuple.Create(0,0);
            var distances = new List<int>();

            foreach (Tuple<int,int> point in intersections)
            {
                var a = Math.Abs(origin.Item1 - point.Item1);
                var b = Math.Abs(origin.Item2 - point.Item2);
                distances.Add(a + b);
            }

            distances.Sort();

            return distances[0];
        }

        public static void Run(string filePath, Logger log)
        {
            var coordList = new List<string[]>();
            var lines = File.ReadLines(filePath, Encoding.UTF8);
            foreach (string line in lines)
            {
                coordList.Add(line.Split(","));
            }

            var sol = new Solution1();
            var wirePathOne = sol.GetWireLayout(coordList[0]);
            var wirePathTwo = sol.GetWireLayout(coordList[1]);
            var intersections = sol.FindIntersections(wirePathOne, wirePathTwo);
            var distance = sol.GetClosestDistance(intersections);
            
            log.Information($"Distance is: {distance}");
        }
    }
}