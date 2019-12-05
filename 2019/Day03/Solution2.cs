using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;

namespace Day03
{
    public class Solution2 : Solution1, ISolution
    {
        public int FindSteps(
            List<Tuple<int,int>> wireOne,
            List<Tuple<int,int>> wireTwo,
            HashSet<Tuple<int,int>> intersections)
        {
            var interOneWithSteps = new List<Tuple<int,int,int>>();
            var interTwoWithSteps = new List<Tuple<int,int,int>>();
            foreach (var intersection in intersections)
            {
                var steps = 0;
                foreach(var point1 in wireOne)
                {
                    steps++;
                    if (point1.Item1 == intersection.Item1)
                        if (point1.Item2 == intersection.Item2)
                            interOneWithSteps.Add(
                                Tuple.Create(point1.Item1, point1.Item2, steps));
                }

                steps = 0;
                foreach(var point2 in wireTwo)
                {
                    steps++;
                    if (point2 == intersection)
                        interTwoWithSteps.Add(
                            Tuple.Create(point2.Item1, point2.Item2, steps));
                }
            }

            var stepList = new List<int>();
            foreach (var point1 in interOneWithSteps)
            {
                foreach (var point2 in interTwoWithSteps)
                {
                    if (point1.Item1 == point2.Item1)
                        if (point1.Item2 == point2.Item2)
                            stepList.Add(point1.Item3 + point2.Item3);
                }
            }

            stepList.Sort();
            return stepList[0];
        }

        new public static void Run(string filePath, Logger log)
        {
            var coordList = new List<string[]>();
            var lines = File.ReadLines(filePath, Encoding.UTF8);
            foreach (string line in lines)
            {
                coordList.Add(line.Split(","));
            }

            var sol = new Solution2();
            var wirePathOne = sol.GetWireLayout(coordList[0]);
            var wirePathTwo = sol.GetWireLayout(coordList[1]);
            var intersections = sol.FindIntersections(wirePathOne, wirePathTwo);
            var steps = sol.FindSteps(wirePathOne, wirePathTwo, intersections);

            log.Information($"Least amount of steps are: {steps}");
        }
    }
}