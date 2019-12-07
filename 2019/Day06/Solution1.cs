using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;
using System.Linq;

namespace Day06
{
    // Planet class that stores the name
    // and parent node that is considered
    // the planet it is orbiting around.
    public class Planet
    {
        public string name;
        public Planet parent;

        public Planet(string name)
        {
            this.name = name;
        }

        // Method traverses through the parents and
        // uses recursion to count the number of parent
        // nodes linked together.
        public int CountOrbits()
        {
            return 1 + parent?.CountOrbits() ?? 0;
        }
    }

    public class Solution1 : ISolution
    {
        // Generates a dictionary of strings associated with Planet objects
        // that have parent and child node relations.
        public Dictionary<string, Planet> GenerateOrbitalMap(
            List<Tuple<string, string>> planets)
        {
            var orbitalSystem = new Dictionary<string, Planet>();
            foreach (var planet in planets)
            {
                Planet parentNode;
                Planet childNode;
                string parent = planet.Item1;
                string child = planet.Item2;

                if (orbitalSystem.ContainsKey(parent))
                {
                    parentNode = orbitalSystem[parent];
                }
                else
                {
                    parentNode = new Planet(parent);
                    orbitalSystem[parent] = parentNode;
                }

                if (orbitalSystem.ContainsKey(child))
                {
                    childNode = orbitalSystem[child];
                    if (childNode.parent == null) childNode.parent = parentNode;
                }
                else
                {
                    childNode = new Planet(child);
                    childNode.parent = parentNode;
                    orbitalSystem[child] = childNode;
                }
            }

            return orbitalSystem;
        }

        // Find the total number of orbits by 
        // traversing through the Planet map.
        public int TotalOrbits(Dictionary<string, Planet> orbits)
        {
            var totals = new List<int>();
            foreach (var planet in orbits.Values)
            {
                totals.Add(planet.CountOrbits());
            }

            return totals.Sum();
        }

        // Takes file input and converts it to a list
        // of Tuples that show parent and child relationships
        // between planet orbits.
        public List<Tuple<string, string>> GenerateInput(string filePath)
        {
            var orbits = new List<Tuple<string, string>>();
            var lines = File.ReadLines(filePath, Encoding.UTF8);
            foreach (string line in lines)
            {
                var planets = line.Split(")");
                orbits.Add(Tuple.Create(planets[0], planets[1]));
            }

            return orbits;
        }

        public static void Run(string filePath, Logger log)
        {
            var sol = new Solution1();
            var orbits = sol.GenerateInput(filePath);
            var orbitalSystem = sol.GenerateOrbitalMap(orbits);
            var total = sol.TotalOrbits(orbitalSystem);
            log.Information($"Total fuel required: {total}");
        }
    }
}