'''
Part 1 find first and last digits and combine them into 2 digit number.
add all 2 digit numbers of the lines.


firstDigit = ''
secondDigit = ''
total = 0

with open('2023\Day1\Day1.txt', 'r') as file:
    for line in file:
        tempList = list(line.strip())
        for i in tempList:
            if i.isnumeric():
                if firstDigit == '':
                    firstDigit = i
                else:
                    secondDigit = i
        if secondDigit == '':
            secondDigit = firstDigit
        tempnum = (int(firstDigit) * 10) + int(secondDigit)
        total = total + tempnum
        tempnum = 0
        firstDigit = ''
        secondDigit = ''

#print(total)
# Answer was 53651
'''
'''
Part 2 - same as above except digits can be spelt out (i.e. 'one', 'two', etc.)
'''

checks = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
results = []
total = 0

def convertLine(l):
    l = l.replace('one', 'o1e')
    l = l.replace('two', 't2o')
    l = l.replace('three', 't3ree')
    l = l.replace('four', 'f4ur')
    l = l.replace('five', 'f5ve')
    l = l.replace('six', 's6x')
    l = l.replace('seven', 's7ven')
    l = l.replace('eight', 'e8ght')
    l = l.replace('nine', 'n9ne')
    return l

total = 0
firstDigit = ''
secondDigit = ''

with open('2023\Day1\Day1.txt', 'r') as file:
    for line in file:
        newline = list(convertLine(line.strip()))
        #print(newline)
        for i in newline:
            if i.isnumeric():
                if firstDigit == '':
                    firstDigit = i
                else:
                    secondDigit = i
        if secondDigit == '':
            secondDigit = firstDigit
        tempnum = (int(firstDigit) * 10) + int(secondDigit)
        total = total + tempnum
        tempnum = 0
        firstDigit = ''
        secondDigit = ''

print(total)

# Answer was 53894