using System.Collections.Generic;

namespace Utils
{
    public class Counter
    {
        private readonly string Message;

        public Counter(string message)
        {
            Message = message;
        }

        public Dictionary<char, int> CountChars()
        {
            Dictionary<char, int> counted = new Dictionary<char, int>();

            foreach (char letter in Message)
            {
                if (counted.ContainsKey(letter))
                {
                    counted[letter]++;
                }
                else
                {
                    counted[letter] = 1;
                }
            }

            return counted;
        }
    }
}
