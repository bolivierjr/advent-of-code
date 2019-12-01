using System;
using System.Diagnostics;

namespace AdventOfCode2019
{
    class Program
    {
        static void Main(string[] args)
        {
            if(args.Length > 2 || args.Length < 2)
            {
                Console.WriteLine("This only takes 2 arguments:");
                Console.WriteLine("========> i.e. dotnet run -- Day01 Solution1");
                return;
            }

            string day = args[0];
            string solution = args[1];

            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            try
            {
                Type type = Type.GetType($"{day}.{solution}");
                type.GetMethod("Run").Invoke(null, null);
            }
            catch (NullReferenceException)
            {
                Console.WriteLine("Cannot find that day and/or solution.");
            }

            stopwatch.Stop();
            Console.WriteLine($"Time Completed: {stopwatch.Elapsed}");
        }
    }
}
