file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

class Node:
    def __init__(self , x , y , height):
        self.x = x
        self.y = y
        self.height = height
        self.children = set()
        self.parent = None
        self.length = 0

    def generate(self , other):
        #print(self.x , self.y , other.x , other.y)
        if(other.height - self.height <= 1 and other.getparent() == None):
            other.setparent(self)
            self.children.add(other)
            other.setlength(self.length + 1)
        elif(other.height - self.height <= 1 and other.length > self.length):
            other.parent.children.remove(other)
            other.setparent(self)
            self.children.add(other)
            other.setlength(self.length + 1)

    def getheight(self):
        return self.height
    
    def setparent(self , other):
        self.parent = other

    def getparent(self):
        return self.parent

    def setlength(self , length):
        self.length = length

    def spantree(self):
        if(self.x > 0):
            self.generate(mountain[self.x-1][self.y])
        if(self.x < rows-1):
            self.generate(mountain[self.x+1][self.y])
        if(self.y > 0):
            self.generate(mountain[self.x][self.y-1])
        if(self.y < width-1):
            self.generate(mountain[self.x][self.y+1])

    def clear(self):
        self.children = set()
        self.parent = None
        self.length = 0
            
def find_len(x , y):
    levels = list()
    level = set()
    level.add(mountain[x][y])
    levels.append(level)

    count = 0
    found = False

    while not(found):
        temp = set()
        count += 1
        for i in level:
            i.spantree()
            for j in i.children:
                temp.add(j)
        level = temp
        for i in levels:
            level = level.difference(i)
        levels.append(level)
        if len(level) == 0:
            return -1
        for i in level:
            if i.x == finish[0] and i.y == finish[1]:
                found = True
    #print(count)
    return count

start = 0
finish = 0

mountain = list()
width = len(lines[0])
rows = len(lines)
possible_starts = list()

i = 0
for i in range (len(lines)):
    temp = list()
    j = 0
    for j in range (len(lines[i])):
        if(lines[i][j] == "S"):
            possible_starts.append([i , j])
            temp.append(Node(i,j,1))
        elif(lines[i][j] == "E"):
            finish = [i,j]
            temp.append(Node(i,j,26))
        else:
            temp.append(Node(i,j , ord(lines[i][j]) - 96))
        if(lines[i][j] == "a"):
            possible_starts.append([i , j])
    mountain.append(temp)

#print(possible_starts)
  
smallest = 350

#print(len(possible_starts))

for i in possible_starts:
    for a in mountain:
        for b in a:
            b.clear()
    res = find_len(i[0] , i[1])
    if res < smallest and res != -1:
        smallest = res

print("Smallest = " , smallest)