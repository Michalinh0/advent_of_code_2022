file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

for line in lines:
    line = line.replace("\n" ,"")