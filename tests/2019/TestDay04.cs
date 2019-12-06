using System;
using Xunit;

namespace tests
{
    public class TestDay04
    {
        [Fact]
        public void TestSolutionOne()
        {
            var range = new string[] { "111110", "111111" };
            var range2 = new string[] { "123455", "123456" };
            var range3 = new string[] { "444554", "444556" };
            var solution1 = new Day04.Solution1();
            int passwords = solution1.FindPasswords(range);
            int passwords2 = solution1.FindPasswords(range2);
            int passwords3 = solution1.FindPasswords(range3);

            Assert.Equal(1, passwords);
            Assert.Equal(1, passwords2);
            Assert.Equal(2, passwords3);
        }

        [Fact]
        public void TestSolutionTwo()
        {
            var range = new string[] { "111333", "111336" };
            var range2 = new string[] { "123455", "123456" };
            var range3 = new string[] { "444555", "444556" };
            var solution2 = new Day04.Solution2();
            int passwords = solution2.FindPasswords(range);
            int passwords2 = solution2.FindPasswords(range2);
            int passwords3 = solution2.FindPasswords(range3);

            Assert.Equal(3, passwords);
            Assert.Equal(1, passwords2);
            Assert.Equal(1, passwords3);
        }
    }
}
