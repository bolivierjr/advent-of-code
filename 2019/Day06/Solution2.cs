using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Interfaces;
using Serilog.Core;
using System.Linq;

namespace Day06
{
    public class Solution2 : Solution1, ISolution
    {
        // Takes two Hashsets as parameters, finds the common paths
        // with intersection, and sorts the Hashset by Planet path 
        // route to root(COM). Takes the last common planet and finds
        // the difference between each parameter route distance
        // traveled and adds them together to get he total difference
        // traveled between the two parameters. Subtract the total by
        // two to count out the parameter nodes.
        public int GetDistance(
            HashSet<Planet> distance1, HashSet<Planet> distance2)
        {
            // Finds the intersecting planets between two paths with Linq.
            var commonPaths = from distance in distance1.Intersect(distance2)
                              select distance;

            var sortCommonPaths = commonPaths.OrderBy(x => x.PathToCom().Count);
            var lastCommonPath = sortCommonPaths.Last().PathToCom();
            int distanceToLastPath1 = distance1.Count - lastCommonPath.Count;
            int distanceToLastPath2 = distance2.Count - lastCommonPath.Count;

            return distanceToLastPath1 + distanceToLastPath2 - 2;
        }

        new public static void Run(string filePath, Logger log)
        {
            var sol = new Solution2();
            var orbits = sol.GenerateInput(filePath);
            var orbitalSystem = sol.GenerateOrbitalMap(orbits);
            var youRoute = orbitalSystem["YOU"].PathToCom();
            var santaRoute = orbitalSystem["SAN"].PathToCom();
            var pathToSanta = sol.GetDistance(youRoute, santaRoute);

            log.Information($"Total is: {pathToSanta}");
        }
    }
}
