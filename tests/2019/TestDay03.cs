using System;
using System.Collections.Generic;
using Xunit;

namespace tests
{
    public class TestDay03
    {
        public string[] wire1 = {"R75","D30","R83","U83","L12","D49","R71","U7","L72"};
        public string[] wire2 = {"U62","R66","U55","R34","D71","R55","D58","R83"};
        public string[] wire3 = {"R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"};
        public string[] wire4 = {"U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"};
    
        [Fact]
        public void TestSolutionOne()
        {
            var solution1 = new Day03.Solution1();
            var wirePath1 = solution1.GetWireLayout(wire1);
            var wirePath2 = solution1.GetWireLayout(wire2);
            var intersections1 = solution1.FindIntersections(wirePath1, wirePath2);
            var distance1 = solution1.GetClosestDistance(intersections1);

            var wirePath3 = solution1.GetWireLayout(wire3);
            var wirePath4 = solution1.GetWireLayout(wire4);
            var intersections2 = solution1.FindIntersections(wirePath3, wirePath4);
            var distance2 = solution1.GetClosestDistance(intersections2);
            
            Assert.Equal(159, distance1);
            Assert.Equal(135, distance2);
        }

        [Fact]
        public void TestSolutionTwo()
        {
            var solution2 = new Day03.Solution2();
            var wirePath1 = solution2.GetWireLayout(wire1);
            var wirePath2 = solution2.GetWireLayout(wire2);
            var intersections1 = solution2.FindIntersections(wirePath1, wirePath2);
            var steps1 = solution2.FindSteps(wirePath1, wirePath2, intersections1);

            var wirePath3 = solution2.GetWireLayout(wire3);
            var wirePath4 = solution2.GetWireLayout(wire4);
            var intersections2 = solution2.FindIntersections(wirePath3, wirePath4);
            var steps2 = solution2.FindSteps(wirePath3, wirePath4, intersections2);

            Assert.Equal(610, steps1);
            Assert.Equal(410, steps2);
        }
    }
}