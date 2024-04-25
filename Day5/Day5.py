seedsList = []
mapFlag = 0
mapDict = {
    'seed-to-soil':  [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}

with open('Day5.txt') as file:
    for line in file:
        newline = line.strip().split(' ')
        #print(newline)

        # Part 1
        #if newline[0] == 'seeds:':
        #    for i in range(1, len(newline)):
        #        seedsList.append(newline[i])
        
        # Part 2
        if newline[0] == 'seeds:':
            for i in range(int(newline[1]), (int(newline[1]) + int(newline[2]))):
                seedsList.append(i)


        if len(newline) > 1 and newline[1] == 'map:':
            mapstr = newline[0]
        
        if newline[0].isnumeric() and mapstr != '':
            mapDict[mapstr].append(newline)
        elif newline[0].isnumeric() and mapstr == '':
            print('Error!')
        
        if newline[0] == ' ':
            mapstr = ''

def findMappedValue(seed, mapList):
    newSeed = 0
    mapFound = False

    for m in mapList:
        if int(m[1]) <= seed < (int(m[1]) + int(m[2])):
            adjustment = int(m[0]) - int(m[1])
            newSeed = seed + adjustment
            mapFound = True
    
    if mapFound == False:
        newSeed = seed
    
    return newSeed


#for key in mapDict:
#    print(key, mapDict[key])

locationList = []

for x in seedsList:
    val = int(x)
    for key in mapDict:
        val = findMappedValue(val, mapDict[key])
    locationList.append(val)

locationList.sort()
print(locationList[0])

# Correct answer was 579439039

