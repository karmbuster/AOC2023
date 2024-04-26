grid = []
r = []
checkNumStr = ''
total = []


with open('2023\Day3\Day3.txt', 'r') as file:
    for line in file:
        line = list(line.strip())
        for x in line:
            r.append(x)
        grid.append(r)
        r = []
    
    

#for x in grid:
#    print(x)

def checkPartNumber(r, c, g, s): # row, columnlist, grid, str (aka the number)
    coordList = []
    for x in c:
        if r > 0:
            if x > 0:
                if (r-1,x-1) not in coordList:
                    coordList.append((r-1,x-1))
            if (r-1, x) not in coordList:
                coordList.append((r-1, x))
            if x < (len(g[0])-1):
                if (r-1,x+1) not in coordList:
                    coordList.append((r-1,x+1))

        if r < (len(grid)-1):
            if x > 0:
                if (r+1,x-1) not in coordList:
                    coordList.append((r+1,x-1))
            if (r+1, x) not in coordList:
                coordList.append((r+1, x))
            if x < (len(g[0])-1):
                if (r+1,x+1) not in coordList:
                    coordList.append((r+1,x+1))

        if x > 0:
            if (r,x-1) not in coordList:
                coordList.append((r,x-1))
        if x < (len(g[0])-1):
            if (r,x+1) not in coordList:
                coordList.append((r,x+1))
        
    print(coordList)
        
    for coord in coordList:
        #print(g[coord[0]][coord[1]])
        if (g[coord[0]][coord[1]].isnumeric() == False) and (g[coord[0]][coord[1]] != '.'):
            return True
        
    return False
        
        
        
'''
for row in range(len(grid)):
    colList = []
    for col in range(len(grid[row])):
        if grid[row][col].isnumeric():
            checkNumStr = checkNumStr + grid[row][col]
            colList.append(col)
        else:
            if checkNumStr != '':
                isPart = checkPartNumber(row, colList, grid, checkNumStr)
                if isPart == True:
                    total.append(int(checkNumStr))
                colList = []
                checkNumStr = ''
    if checkNumStr != '':
        isPart2 = checkPartNumber(row, colList, grid, checkNumStr)
        if isPart2 == True:
            total.append(int(checkNumStr))
        colList = []
        checkNumStr = ''

answer = 0
for x in total:
    answer = answer + x

print(answer)
'''
# the correct answer is 512794

'''
Part 2 - find symbols that are adjacent to exactly 2 numbers and multiply them together - add all these multiplications together
'''

def checkPart2(r, c, g): # row num, col num, grid
    coordList = []
    numAdj = 0
    if r > 0:
            if c > 0:
                coordList.append((r-1,c-1))
            coordList.append((r-1, c))
            if c < (len(g[0])-1):
                coordList.append((r-1,c+1))

    if r < (len(grid)-1):
        if c > 0:
            coordList.append((r+1,c-1))
        coordList.append((r+1, c))
        if c < (len(g[0])-1):
            coordList.append((r+1,c+1))

    #if c > 0:
    #    coordList.append((r,c-1))
    #if c < (len(g[0])-1):
    #    coordList.append((r,c+1))
    
    if r > 0:
        if g[r-1][c].isnumeric():
            numAdj += 1
        else:
            if 


    if c > 0:
        if g[r][c-1].isnumeric():
            numAdj += 1
    if c < (len(g[0])-1):
        if g[r][c+1].isnumeric():
            numAdj += 1
        


    for coord in coordList:
        if grid[coord[0]][coord[1]].isnumeric():
            print(grid[coord[0]][coord[1]])



for row in range(len(grid)):
    for col in range(len(grid[row])):
        if (grid[row][col].isnumeric() == False) and (grid[row][col] != '.'):
            checkPart2(row, col, grid)

