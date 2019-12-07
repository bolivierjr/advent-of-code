using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;
using System.Linq;

namespace Day06
{
    // Planet tree that stores it's name
    // and parent node of the planet it is
    // considered to be orbiting around.
    public class Planet
    {
        public string name;
        public Planet parent;

        public Planet(string name)
        {
            this.name = name;
        }

        // Traverses through the parent nodes and
        // uses DFS to count the number of parent
        // nodes linked together.
        public int CountOrbits()
        {
            return 1 + parent?.CountOrbits() ?? 0;
        }

        // Traverses through the parent nodes using
        // BFS with a queue and returns a hashset of
        // the nodes.
        public HashSet<Planet> PathToCom()
        {
            var distance = new HashSet<Planet>();
            var queue = new Queue<Planet>();
            queue.Enqueue(this);
            while (queue.Count > 0)
            {
                var currentNode = queue.Dequeue();
                distance.Add(currentNode);
                if (currentNode.parent != null)
                {
                    queue.Enqueue(currentNode.parent);
                }
            }

            return distance;
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
                    childNode.parent = parentNode;
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
        public int TotalOrbits(Dictionary<string, Planet> orbitalSystem)
        {
            var totals = new List<int>();
            foreach (var planet in orbitalSystem.Values)
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
            log.Information($"Total is: {total}");
        }
    }
}
