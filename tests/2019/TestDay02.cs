using System;
using Xunit;

namespace tests
{
    public class TestDay02
    {
        public int[] optcodeNums = { 1, 1, 1, 4, 99, 5, 6, 0, 99 };

        [Fact]
        public void TestSolutionOne()
        {
            Day02.Solution1 solution1 = new Day02.Solution1();
            int processed = solution1.OptcodeProcessor(optcodeNums);

            Assert.Equal(30, processed);
        }

        [Fact]
        public void TestSolutionTwo()
        {

        }
    }
}