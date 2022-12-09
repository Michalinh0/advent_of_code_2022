file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

uniquepositions = set()

rope = list()

for i in range(10):
    rope.append([100 , 100])


for line in lines:
    line = line.split(" ")
    #print(line)
    for i in range(int(line[1])):
        if(line[0] == "U"):
            rope[0][1] -= 1
        if(line[0] == "D"):
            rope[0][1] += 1
        if(line[0] == "L"):
            rope[0][0] -= 1
        if(line[0] == "R"):
            rope[0][0] += 1
        for j in range(1,10):

            if(rope[j][0] - rope[j-1][0] == 2):
                rope[j][0] = rope[j][0] - 1
                if(rope[j][1] - rope[j-1][1] < 0):
                    rope[j][1] += 1
                elif(rope[j][1] - rope[j-1][1] > 0):
                    rope[j][1] -= 1

            elif(rope[j][0] - rope[j-1][0] == -2):
                rope[j][0] = rope[j][0] + 1
                if(rope[j][1] - rope[j-1][1] < 0):
                    rope[j][1] += 1
                elif(rope[j][1] - rope[j-1][1] > 0):
                    rope[j][1] -= 1

            elif(rope[j][1] - rope[j-1][1] == 2):
                rope[j][1] = rope[j][1] - 1
                if(rope[j][0] - rope[j-1][0]  < 0):
                    rope[j][0] += 1
                elif(rope[j][0] - rope[j-1][0] > 0):
                    rope[j][0] -= 1

            elif(rope[j][1] - rope[j-1][1] == -2):
                rope[j][1] = rope[j][1] + 1
                if(rope[j][0] - rope[j-1][0] < 0):
                    rope[j][0] += 1
                elif(rope[j][0] - rope[j-1][0] > 0):
                    rope[j][0] -= 1

        uniquepositions.add((rope[9][0] , rope[9][1]))
        #print("\n" ,rope)
        #print("----")
    print(rope)
    #print("------------")
print(len(uniquepositions))