file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

trees = list()

i = 0
for i in range(len(lines)):
    temp = list()
    for j in range(len(lines[i])):
        temp.append(int(lines[i][j]))
    trees.append(temp)

print(len(trees) , len(trees[0]))

vistrees = [ [0]*len(trees) for i in range(len(trees))]

for row in range(len(trees)):
    highest = -1
    for column in range(len(trees)):
        if(trees[row][column] > highest):
            vistrees[row][column] = 1
            highest = trees[row][column]


for row in range(len(trees)):
    highest = -1
    for column in range(len(trees)):
        if(trees[column][row] > highest):
            vistrees[column][row] = 1
            highest = trees[column][row]


for row in range(len(trees)):
    highest = -1
    for column in range(len(trees)):
        if(trees[row][len(trees[i]) - 1 - column] > highest):
            vistrees[row][len(trees[i]) - 1 - column] = 1
            highest = trees[row][len(trees[i]) - 1 - column]


for row in range(len(trees)):
    highest = -1
    for column in range(len(trees)):
        if(trees[len(trees) - 1 - column][row] > highest):
            vistrees[len(trees) - 1 - column][row] = 1
            highest = trees[len(trees) - 1 - column][row]

count = 0
for i in range(len(trees)):
    for j in range(len(trees)):
        count += vistrees[i][j]

print(count)

scores = [ [0]*len(trees) for i in range(len(trees))]

highestscore = -1

for i in range(len(trees)):
    for j in range(len(trees)):
        if(i == 0 or j == 0 or i == len(trees)-1 or j == len(trees)-1):
            scores[i][j] = -1
        else:
            score = list()

            count = 0
            x = i-1
            while(x >= 0):
                if(trees[x][j] >= trees[i][j]):
                    count +=1
                    break
                else:
                    count +=1
                    x -= 1
            #print(count)
            score.append(count)

            x = i + 1
            count = 0
            while(x < len(trees)):
                if(trees[x][j] >= trees[i][j]):
                    count +=1
                    break
                else:
                    count +=1
                    x += 1
            #print(count)
            score.append(count)

            count = 0
            y = j-1
            while(y >= 0):
                if(trees[i][y] >= trees[i][j]):
                    count +=1
                    break
                else:
                    count +=1
                    y -= 1
            #print(count)
            score.append(count)

            y = j + 1
            count = 0
            while(y < len(trees)):
                if(trees[i][y] >= trees[i][j]):
                    count +=1
                    break
                else:
                    count +=1
                    y += 1
            #print(count)
            score.append(count)

            scores[i][j] = score[0] * score[1] * score[2] * score[3]
            if(scores[i][j]) > highest:
                highest = scores[i][j]


print(highest)
