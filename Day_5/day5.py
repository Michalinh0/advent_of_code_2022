file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

stacks = list()
for i in range(9): # 9
    stacks.append(list())

for i in range(8): # 8
    for j in range(9): # 9
        if(lines[i][j*4+1]!= " "):
            stacks[j].append(lines[i][j*4 + 1])

for i in range(9):
    stacks[i].reverse()

for line in lines:
    if("move" in line):
        ints = [int(s) for s in line.split() if s.isdigit()]
        for i in range(ints[0]):
            if(len(stacks[ints[1]-1]) > 0):
                stacks[ints[2]-1].append(stacks[ints[1]-1].pop())

for i in range(9):
    print(stacks[i][len(stacks[i])-1])