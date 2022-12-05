file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

set1 = set()
set2 = set()
set3 = set()

curr = 0
mod = 0

for line in lines:
    line = line.replace("\n" ,"")
    if(mod == 3):
        set1 = set()
        set2 = set()
        set3 = set()
        mod = 0
    mod += 1
    for char in line:
        if(mod == 1):
            set1.add(char)
        elif(mod == 2):
            set2.add(char)
        else:
            set3.add(char)
    inter = set1.intersection(set2)
    inter = inter.intersection(set3)
    for i in inter:
        if(ord(i) < 97):
            curr += (ord(i) - 38)
            print()
        else:
            curr += (ord(i) - 96)
            print()

print(curr)