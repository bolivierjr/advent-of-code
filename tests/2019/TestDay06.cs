using System;
using System.Collections.Generic;
using Xunit;

namespace tests
{
    public class TestDay06
    {
        [Fact]
        public void TestSolutionOne()
        {
            var input = new List<Tuple<string, string>> {
                Tuple.Create("COM","B"), Tuple.Create("B","C"), Tuple.Create("C","D"), Tuple.Create("D","E"),
                Tuple.Create("E","F"), Tuple.Create("B","G"), Tuple.Create("G","H"), Tuple.Create("D","I"),
                Tuple.Create("E","J"), Tuple.Create("J","K"), Tuple.Create("K","L")};

            var solution1 = new Day06.Solution1();
            var orbitalSystem = solution1.GenerateOrbitalMap(input);
            var total = solution1.TotalOrbits(orbitalSystem);

            Assert.Equal(42, total);
        }

        [Fact]
        public void TestSolutionTwo()
        {
            var newInput = new List<Tuple<string, string>> {
                Tuple.Create("COM","B"), Tuple.Create("B","C"), Tuple.Create("C","D"), Tuple.Create("D","E"),
                Tuple.Create("E","F"), Tuple.Create("B","G"), Tuple.Create("G","H"), Tuple.Create("D","I"),
                Tuple.Create("E","J"), Tuple.Create("J","K"), Tuple.Create("K","L"), Tuple.Create("K", "YOU"),
                Tuple.Create("I", "SAN")};


            var solution2 = new Day06.Solution2();
            var orbitalSystem = solution2.GenerateOrbitalMap(newInput);
            var you = orbitalSystem["YOU"];
            var santa = orbitalSystem["SAN"];
            var youRoute = you.PathToCom();
            var santaRoute = santa.PathToCom();
            var pathToSanta = solution2.GetDistance(youRoute, santaRoute);

            Assert.Equal(4, pathToSanta);
        }
    }
}
