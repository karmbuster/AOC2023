with open("day9.txt", encoding="utf-8") as myFile:
    for line in myFile.readlines():
        lineList = line.strip().split()
        newList = []
        print(len(set(newList)))
        while len(set(newList)) != 1:
            for num in range(1, len(lineList)):
                print(lineList[num])
                newList.append(int(lineList[num]) - int(lineList[num - 1]))
            print(newList)
            newList = []

        print("here")


# use any(list) to see if list has all zeros
