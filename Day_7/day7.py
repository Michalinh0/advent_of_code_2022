#file = open("input.txt" , 'r')
file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

class Directory:
    def __init__(self, parent , name):
        self.parent = parent
        self.children = list()
        self.name = name
    
    def Size(self):
        sum = 0
        for i in self.children:
            sum += i.Size()
        return sum

    def Parent(self):
        return self.parent

    def append(self , other):
        self.children.append(other)

    def findchild(self, name):
        for i in self.children:
            if(isinstance(i , Directory)):
                if(i.Name() == name):
                    return i
    
    def Name(self):
        return self.name

class File:
    def __init__(self , size , name):
        self.size = size
        self.name = name
    
    def Size(self):
        return self.size

dirlist = list([Directory(None , "/")])
active = dirlist[0]

for line in lines:
    line = line.split(" ")
    #print(line , active)
    if(line[1] == "cd"):
        if(line[2] == "/"):
            continue
        elif(line[2] == ".."):
            active = active.Parent()
        else:
            active = active.findchild(line[2])
    elif(line[0] == "dir"):
        newdir = Directory(active , line[1])
        dirlist.append(newdir)
        active.append(newdir)
    elif(line[0] == "$"):
        continue
    else:
        active.append(File(int(line[0]) , line[1]))

#print(dirlist)

sums = list()
for i in dirlist:
    sums.append(i.Size())

count = 0
for i in sums:
    if(i < 100000):
        count += i
print(sums)

free = 70000000 - sums[0]
required = 30000000

smallest = 70000000
for i in sums:
    if(free + i > required and i < smallest):
        smallest = i
    
print(count)
print(smallest)

    
            


    