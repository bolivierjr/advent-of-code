using System;
using System.Collections.Generic;
using Xunit;

namespace tests
{
    public class TestDay03
    {
        public string[] wireOne = {"R75","D30","R83","U83","L12","D49","R71","U7","L72"};
        public string[] wireTwo = {"U62","R66","U55","R34","D71","R55","D58","R83"};
        [Fact]
        public void TestSolutionOne()
        {
            var solution1 = new Day03.Solution1();
            var wirePathOne = solution1.GetWireLayout(wireOne);
            var wirePathTwo = solution1.GetWireLayout(wireTwo);

            var expected1 = new List<Tuple<int,int>>() {
                Tuple.Create(75,-30),Tuple.Create(83,83),Tuple.Create(-12,-49),Tuple.Create(71,7)};
            var expected2 = new List<Tuple<int,int>>() {
                Tuple.Create(62, 66),Tuple.Create(55,34),Tuple.Create(-71,55),Tuple.Create(-58,83)};

            Assert.Equal(expected1, wirePathOne);
            Assert.Equal(expected2, wirePathTwo);
        }

        [Fact]
        public void TestSolutionTwo()
        {
        }
    }
}