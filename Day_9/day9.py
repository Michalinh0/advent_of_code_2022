file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

head = [100 , 100]
tail = [100 , 100]

uniquepositions = set()
uniquepositions.add((100 , 100))

for line in lines:
    line = line.split(" ")
    print(line)
    for i in range(int(line[1])):
        #print("before : " , head , tail)
        if(line[0] == "U"):
            temp = head[:]
            head[1] -= 1
            if(abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2):
                tail = temp
            uniquepositions.add((tail[0] , tail[1]))
        if(line[0] == "L"):
            temp = head[:]
            head[0] -= 1
            if(abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2):
                tail = temp
            uniquepositions.add((tail[0] , tail[1]))
        if(line[0] == "D"):
            temp = head[:]
            head[1] += 1
            if(abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2):
                tail = temp
            uniquepositions.add((tail[0] , tail[1]))
        if(line[0] == "R"):
            temp = head[:]
            head[0] += 1
            if(abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2):
                tail = temp
            uniquepositions.add((tail[0] , tail[1]))
        print(temp)

#print(uniquepositions)
print(len(uniquepositions))

