using System;
using System.Collections.Generic;
using Xunit;

namespace tests
{
    public class TestDay06
    {
        public List<Tuple<string, string>> input = new List<Tuple<string, string>> {
            Tuple.Create("COM","B"), Tuple.Create("B","C"), Tuple.Create("C","D"), Tuple.Create("D","E"),
            Tuple.Create("E","F"), Tuple.Create("B","G"), Tuple.Create("G","H"), Tuple.Create("D","I"),
            Tuple.Create("E","J"), Tuple.Create("J","K"), Tuple.Create("K","L")};

        [Fact]
        public void TestSolutionOne()
        {
            var solution1 = new Day06.Solution1();
            var orbitalSystem = solution1.GenerateOrbitalMap(input);
            var total = solution1.TotalOrbits(orbitalSystem);

            Assert.Equal(42, total);
        }

        [Fact]
        public void TestSolutionTwo()
        {
            // var solution1 = new Day06.Solution2();
            // var orbitalSystem = solution2.GenerateOrbitalMap(input);

            Assert.Equal(42, 1);
        }
    }
}
