using System;
using Xunit;

namespace tests
{
    public class TestDay01
    {
        public int[] masses = { 12, 14, 1969, 100756 };

        [Fact]
        public void TestSolutionOneRequiredFuel()
        {
            Day01.Solution1 solution1 = new Day01.Solution1();

            foreach (int mass in masses)
            {
                solution1.RequiredFuel(mass);
            }

            Assert.Equal(34_241, solution1.TotalFuel);
        }

        [Fact]
        public void TestSolutionTwoRequiredFuel()
        {
            Day01.Solution2 solution2 = new Day01.Solution2();

            foreach (int mass in masses)
            {
                solution2.RequiredFuel(mass);
            }

            Assert.Equal(51_316, solution2.TotalFuel);
        }
    }
}
