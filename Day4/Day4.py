
score = 0
total = 0
scoreList = [0]*220
ind = 0

with open('2023\Day4\Day4.txt', 'r') as file:
    for line in file:
        line = line.strip().split('|')
        winningList = line[0].split(' ')
        #print(winningList)
        for i in winningList:
            if i.isnumeric() == False:
                winningList.remove(i)
        #print(winningList)

        currentNumbers = line[1].split(' ')
        for i in currentNumbers:
            if i.isnumeric() == False:
                currentNumbers.remove(i)
        #print(currentNumbers)
        
        score = 0
        for j in currentNumbers:
            if j.isnumeric()==True and j in winningList:
                    score += 1

        # Part 1 find the total of the scores
        # scores are 1 for the first then double the score for each additional match
        # 1 match = 1, 2 matches = 2, 3 matches = 4, 4 matches = 8
        # not needed for part 2
        #if score > 0:
        #    total = total + (2**(score - 1))

        # Part 2
        # find how many scratchcards you win
        # if you have x number of matches then you win that scorecard and one copy each of the next scorecards
        # if you win scorecard 1 with 4 matches then you win card 1 and copies of the next 4
        # if you win scorecard 2 then you have won scorecard 2 plus again due to the copy you won from card 1 and so on

        if score > 0:
             # add one to score for that card due to winning that card
            scoreList[ind] += 1

            for z in range(1, score):
                scoreList[ind + z] += 1
        

            
            

        # incrememnt index keeping track of what card
        ind += 1

print(scoreList)

#print(total)

# correct answer is 28538

        
