file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

strength = 0
cycle = 0
value = 1

for line in lines:
    line = line.split(" ")
    #print(line)
    if line[0] == "noop":
        if cycle % 40 == 19:
            strength += value * (cycle + 1)
            #print(cycle , value)
        cycle += 1
    if line[0] == "addx":
        if cycle % 40 == 19:
            strength += value * (cycle + 1)
            #print(cycle , value)
        cycle += 1
        if cycle % 40 == 19:
            strength += value * (cycle + 1)
            #print(cycle , value)
        cycle += 1
        value += int(line[1])

register = 1
cycle = 0
image = list()
string = ""

for line in lines:
    line = line.split(" ")
    if(cycle % 40 == 0):
        image.append(string)
        string = ""
    position = cycle % 40
    if line[0] == "noop":
        print(register -1 , position , register + 1)
        if(register - 1 <= position <= register + 1):
            string += "#"
        else:
            string += "."
        cycle += 1
    if line[0] == "addx":
        print(register -1 , position , register + 1)
        if(register - 1 <= position <= register + 1):
            string += "#"
        else:
            string += "."
        cycle += 1
        if(cycle % 40 == 0):
            image.append(string)
            string = ""
        position = cycle % 40
        print(register -1 , position , register + 1)
        if(register - 1 <= position <= register + 1):
            string += "#"
        else:
            string += "."
        cycle += 1
        register += int(line[1])

for i in image:
    print(i)

print(strength)
