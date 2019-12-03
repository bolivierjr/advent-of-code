using System;
using System.IO;
using System.Diagnostics;
using Serilog;
using Serilog.Core;

namespace AdventOfCode2019
{
    class Program
    {
        static void Main(string[] args)
        {
            Logger log = new LoggerConfiguration()
                .WriteTo.Console()
                .CreateLogger();

            if(args.Length > 2 || args.Length < 2)
            {
                log.Information("This only takes 2 arguments:");
                log.Information("========> i.e. dotnet run -- Day01 Solution1");
                return;
            }

            string day = args[0];
            string solution = args[1];
            string filePath = Path.GetFullPath($"{day}/input.txt");

            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            try
            {
                var type = Type.GetType($"{day}.{solution}");
                type.GetMethod("Run").Invoke(null, new object[] {filePath, log});

                stopwatch.Stop();
                log.Information($"Time Completed: {stopwatch.Elapsed}");
            }
            catch (NullReferenceException)
            {
                log.Error("Cannot find that day and/or solution.");
            }

        }
    }
}
