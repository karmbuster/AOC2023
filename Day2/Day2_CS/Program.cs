using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            string path = @"Day2.txt";
            string[] inString = File.ReadAllLines(path);

            String[] colorStr = new String[]{
                "blue",
                "red",
                "green"
            };
            int count = 0;
            // Loop through the input strings - this will be replaced when using the file input
            // In this case start at 1 so I can use index to keep track of which game I am on.
            // this is because I need to add the game numbers up for games that are valid.
            for (int i = 1; i <= inString.Length; i++)
            {
                bool validGame = true;
                int index = i - 1;
                int blueMax = 0;
                int redMax = 0;
                int greenMax = 0;
                foreach (string color in colorStr) // loop through three colors
                {
                    var matches = Regex.Matches(inString[index], @"\d+ " + color);
                    foreach (Match match in matches)
                    {
                        if ((color == "blue") && (Int32.Parse(match.Value.Split(' ')[0]) > 14)
                            || (color == "red") && (Int32.Parse(match.Value.Split(' ')[0]) > 12)
                            || (color == "green") && (Int32.Parse(match.Value.Split(' ')[0]) > 13))
                        {
                            validGame = false;
                        }
                        // Part 2
                        if ((color == "blue")
                            && (Int32.Parse(match.Value.Split(' ')[0]) > blueMax))
                        {
                            blueMax = Int32.Parse(match.Value.Split(' ')[0]);
                        }
                        if ((color == "red")
                            && (Int32.Parse(match.Value.Split(' ')[0]) > redMax))
                        {
                            redMax = Int32.Parse(match.Value.Split(' ')[0]);
                        }
                        if ((color == "green")
                            && (Int32.Parse(match.Value.Split(' ')[0]) > greenMax))
                        {
                            greenMax = Int32.Parse(match.Value.Split(' ')[0]);
                        }
                    }
                }
                // Uncomment for Part 1
                if (validGame ==  true)
                {
                    //Console.WriteLine($"Game {i} is valid");
                    count += i;
                } 
                // Part 2
                //Console.WriteLine($"For Game {i}, the product is {(blueMax * redMax * greenMax)}");
                //count += (blueMax * redMax * greenMax);
            }
            // Part 1
            Console.WriteLine($"The sum of IDs of possible games for Part 1 is {count}");
            // The Answer is 2105
            // Part 2
            //Console.WriteLine($"The sum of products for Part 2 is {count}");
            // The answer for Part 2 is 72422
        }
    }
}


