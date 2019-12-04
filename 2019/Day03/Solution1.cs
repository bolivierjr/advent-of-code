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
        public struct Point
        {
            public int x, y;

            public Point(int p1, int p2)
            {
                x = p1;
                y = p2;
            }
        }

        public List<Point> GetWireLayout(string[] wirepath)
        {
            int xCoord = 0;
            int yCoord = 0;
            var coordinates = new List<Point>();

            foreach(string wire in wirepath)
            {
                var letter = wire.Substring(0, 1);
                var number = Int32.Parse(wire.Substring(1));

                if (letter == "L") xCoord -= number;
                else if (letter == "R") xCoord += number;
                else if (letter == "U") yCoord += number;
                else if (letter == "D") yCoord -= number;

                coordinates.Add(new Point(xCoord, yCoord));
            }

            return coordinates;
        }

        public List<Point> FindIntersections(List<Point> wireOne,List<Point> wireTwo)
        {
            var intersections = new List<Point>();

            for (int indexOne=0; indexOne<wireOne.Count; indexOne+=2)
            {
                for (int indexTwo=0; indexTwo<wireOne.Count; indexTwo+=2)
                {
                    Point A = wireOne[indexOne];
                    Point B = wireOne[indexOne + 1];
                    Point C = wireTwo[indexTwo];
                    Point D = wireTwo[indexTwo + 1];

                    double a1 = B.y - A.y;
                    double b1 = A.x - B.x;
                    double c1 = a1 * (A.x) + b1 * (A.y);
                    double a2 = D.y - C.y;
                    double b2 = C.x - D.x;
                    double c2 = a2 * (C.x) + b2 * (C.y);

                    double det = a1 * b2 - a2 * b1;

                    if (det == 0) continue;

                    double x = (b2 * c1 - b1 * c2) / det;
                    double y = (a1 * c2 - a2 * c1) / det;

                    if (x % Math.Floor(x) != 0) continue;
                    if (y % Math.Floor(y) != 0) continue;

                    intersections.Add(new Point((int)x, (int)y));
                }
            }

            return intersections;
        }

        public int GetClosestDistance(List<Point> intersections)
        {
            var origin = new Point(0,0);
            var distances = new List<int>();

            foreach (Point point in intersections)
            {
                var a = Math.Abs(origin.x - point.x);
                var b = Math.Abs(origin.y - point.y);
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
            
            foreach (Point p in intersections)
            {
                log.Information($"({p.x},{p.y})");
            }
            
            log.Information($"Distance is: {distance}");
        }
    }
}