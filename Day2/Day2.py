'''
Part 1 - add up games id's that are possible with 12 red cubes, 13 green cubes, and 14 blue cubes
'''
'''
total = 0

with open('2023\Day2\Day2.txt', 'r') as file:
    for line in file:
        line = line.strip('')
        newline = line.split()
        print(newline)
        theId = int(newline[1])
        fail = False
        for x in range(len(newline)):
            itemx = x
            item = newline[x]
            if newline[x].find('red') != -1:
                if  int(newline[x - 1]) > 12:
                    fail = True
            if newline[x].find('green') != -1:
                if int(newline[x - 1]) > 13:
                    fail = True
            if newline[x].find('blue') != -1:
                if int(newline[x - 1]) > 14:
                    fail = True
        if fail == False:
            total = total + theId

print(total)

# CORRECT ANSWER for part 1 IS 2105.
'''
'''
Part 2 Find fewest number of cubes required to play each game for each color.  Then multiply the 3 numbers together and add all the multiplied values together.
'''

total = 0

with open('2023\Day2\Day2.txt', 'r') as file:
    for line in file:
        line = line.strip('')
        newline = line.split()
        newline.pop(0)
        newline.pop(0)
        #print(newline)

        minNumCubes = {
            'red': 0,
            'blue': 0,
            'green': 0
        }

        for x in range(len(newline)):
            if newline[x].find('red') != -1:
                if int(newline[x-1]) > minNumCubes['red']:
                    minNumCubes['red'] = int(newline[x-1])
            if newline[x].find('blue') != -1:
                if int(newline[x-1]) > minNumCubes['blue']:
                    minNumCubes['blue'] = int(newline[x-1])
            if newline[x].find('green') != -1:
                if int(newline[x-1]) > minNumCubes['green']:
                    minNumCubes['green'] = int(newline[x-1])
        
        total = total + (minNumCubes['red'] * minNumCubes['blue'] * minNumCubes['green'])

print(total)

# The correct answer for part 2 is 72422
        