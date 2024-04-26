using System;
using System.Text;
using System.IO;

internal class Program
{
    private static void Main(string[] args)
    {
        string path = @"C:\Users\karmb\OneDrive\Documents\Advent of Code\2023\Day1\Day1_CS\Day1.txt";
        using (StreamReader sr = File.OpenText(path))
        {
            string s;
            int total = 0;
            while ((s = sr.ReadLine()) != null)
            {
                char firstDigit = 'a';
                char secondDigit = 'a';
                //Console.WriteLine(s);
                foreach (char letter in s)
                {
                    //Console.WriteLine(letter);
                    if (char.IsNumber(letter))
                    {
                        if (firstDigit == 'a')
                        {
                            firstDigit = letter;
                        }
                        else
                        {
                            secondDigit = letter;
                        }
                    }

                }
                if (secondDigit == 'a')
                {
                    secondDigit = firstDigit;
                }
                int first = firstDigit - '0';
                int second = secondDigit - '0';
                int tempNum = first * 10 + second;
                total += tempNum;
                tempNum = 0;
                firstDigit = 'a';
                secondDigit = 'a';
            }
            Console.WriteLine($"The total for Part 1 is {total}");
            // Part 1 Answer is 53651
        }
        string[] inString = File.ReadAllLines(path);
        string[] replacedString = new string[inString.Length];
        int index = 0;
        foreach (string str in inString)
        {
            string newString = str.Replace("one", "o1e")
                    .Replace("two", "t2o")
                    .Replace("three", "th3ee")
                    .Replace("four", "f4ur")
                    .Replace("five", "f5ve")
                    .Replace("six", "s6x")
                    .Replace("seven", "se7en")
                    .Replace("eight", "ei8ht")
                    .Replace("nine", "n9ne")
                    .Replace("zero", "z0ro");
            replacedString.SetValue(newString, index);
            index++;
        }
        int total2 = 0;
        foreach (string str in replacedString)
        {
            //Console.WriteLine(str);
            char firstDigit = str.First(Char.IsDigit);
            char lastDigit = str.Last(Char.IsDigit);
            int digits = ((firstDigit - '0') * 10) + (lastDigit - '0');
            total2 += digits;
        }
        Console.WriteLine($"The total sum for Part 2 is {total2}");
        // The answer is 53894
    }
}