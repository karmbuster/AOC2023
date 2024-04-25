from math import lcm

# insString is the instruction pattern
insString = "LRRRLLRLLRRLRLRRRLRLRRRLRRLLRRRLRRLRLLRLLRRLRLLLLRRLRRLRLLRRLRRRLLLRRLRLRRLRRRLRRRLLRLRRRLLRRLRRRLRRLRLRRLRRLLRLRLRRRLRRLRRLRRRLRRLRRLRLRRRLRRRLRRRLLLRLRRLRLRRRLRRRLRRLRRLLRLRRLLRRLLRLRRLRLRRLRRRLRLRRLRLRRRLLRRLLRLRRRLRRRLRRRLRRRLLLRLRRLRRRLRRRLRLLRRLLRRLRLRLLRRLRRLLRRRLRLRRRLRRRR"
# convert to list (probably not even necessary since we can get index and length of a string
insArr = list(insString)
dictNode = {}
# For Part 2
startList = []

with open("day8.txt", encoding="utf-8") as myFile:
    for line in myFile.readlines():
        lineList = line.replace("(", "").replace(")", "").replace(",", "").split()
        nodeList = []
        nodeList.append(lineList[2])
        nodeList.append(lineList[3])
        dictNode[lineList[0]] = nodeList
        # for part 2 need all the nodes that end in "A"
        if list(lineList[0])[-1] == "A":
            startList.append(lineList[0])
myFile.close()

print(startList)


# for Part 2
def allEndZ(l):
    # take in a list and return True if all items in the list
    #   end in "Z"
    for x in l:
        if x[-1] != "Z":
            return False
    return True


# next = "AAA"
# index = 0
# count = 1
# Part 1
# while next != "ZZZ":
#    paths = dictNode[next]
#    if index > (len(insArr) - 1):
#        index = 0
#    # print(paths)
#    if insArr[index] == "L":
#        next = paths[0]
#    elif insArr[index] == "R":
#        next = paths[1]
#    else:
#        print("Something is wrong")
#    index = index + 1
#    count = count + 1


# for Part 2 - long way - takes hours to find it.
# check = False
# nextList = startList
# while check == False:
#    if index > (len(insArr) - 1):
#        index = 0
#    tempNextList = []
#    for n in nextList:
#        paths = dictNode[n]
#        if insArr[index] == "L":
#            tempNextList.append(paths[0])
#        elif insArr[index] == "R":
#            tempNextList.append(paths[1])
#        else:
#            print("Something went wrong")
#    if allEndZ(tempNextList):
#        check = True
#    else:
#        index = index + 1
#        count = count + 1
#        nextList = tempNextList

countList = []
for x in startList:
    next = x
    count = 1
    index = 0
    check = False
    nextList = []
    while check == False:
        paths = dictNode[next]
        if index > (len(insArr) - 1):
            index = 0
        if insArr[index] == "L":
            next = paths[0]
        elif insArr[index] == "R":
            next = paths[1]
        else:
            print("Something is wrong")
        nextList.append(next)
        check = allEndZ(nextList)
        if check == False:
            index = index + 1
            count = count + 1
            nextList = []
        else:
            countList.append(count)
print(countList)

print(count)
# Part 1 Answer was 16579

# For Part 2 we had to calculate the number of steps it took for all nodes that end in "A" to all end at nodes that end in "Z"
# in the same number of steps
# apparently the steps are set up in a way that I just had to find the number of steps for each node ending in "A"
# to its corresponding node ending in "Z" and then find the lowest common multiple.
# Need to run with Python 3.12 to work.  lcm not available in Python 3.7
print(lcm(14893, 19951, 22199, 16579, 17141, 12083))
# Part 2 Answer was 12_927_600_769_609 underscores are just for easier reading the number.
