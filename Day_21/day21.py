file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

class Monke:

    number = None
    monke1 = None
    monke2 = None
    operation = None
    parent = None

    def __init__(self, *args):
        if(len(args) == 2):
            self.number = args[1]
        elif(len(args) == 4):
            self.monke1 = args[1]
            self.operation = args[2]
            self.monke2 = args[3]
        else:
            raise ValueError("Wrong number of arguments")
        self.name = args[0]
    
    def independent(self):
        return self.monke1 == self.monke2 == None

    def setmonke1(self, monke):
        self.monke1 = monke
    
    def setmonke2(self, monke):
        self.monke2 = monke

    def getmonke1(self):
        return self.monke1
    
    def getmonke2(self):
        return self.monke2

    def getname(self):
        return self.name

    def getnumber(self):
        if self.number != None:
            return self.number
        else:
            if self.operation == "+":
                return self.monke1.getnumber() + self.monke2.getnumber()
            if self.operation == "-":
                return self.monke1.getnumber() - self.monke2.getnumber()
            if self.operation == "*":
                return self.monke1.getnumber() * self.monke2.getnumber()
            if self.operation == "/":
                return self.monke1.getnumber() / self.monke2.getnumber()
            if self.operation == "=":
                return self.monke1.getnumber() == self.monke2.getnumber()

    def setnumber(self , number):
        self.number = number

    def setparent(self, monke):
        self.parent = monke

    def getpath(self , way):
        way.append(self)
        if(self.name == "root"):
            return way
        else:
            return self.parent.getpath(way)

    
monkes = list()
root = None
me = None

for line in lines:
    line = line.split()
    line[0] = line[0].replace(":" , "")
    if(line[1].isdigit()):
        monkes.append(Monke(line[0] , int(line[1])))
    else:
        monkes.append(Monke(line[0] , line[1] , line[2] , line[3]))
    if(line[0] == "root"):
        root = monkes[-1]
    if(line[0] == "humn"):
        me = monkes[-1]


print("Created monkes")

for monke in monkes:
    if monke.independent() == False:
        monke1 = monke.getmonke1()
        monke2 = monke.getmonke2()
        for monk in monkes:
            if monk.getname() == monke1:
                monke.setmonke1(monk)
                monk.setparent(monke)
            if monk.getname() == monke2:
                monke.setmonke2(monk)
                monk.setparent(monke)

print("Set up monkes")

for monke in monkes:
    pass
    #print(monke.number , monke.monke1 , monke.monke2)

print(root.getnumber())

# Part 2

root.operation = "="

way_to_root = me.getpath(list())

way_to_root.reverse()

print("---------------")

solution = list()

if root.monke1 == way_to_root[1]:
    solution.append(root.monke2.getnumber())
else:
    solution.append(root.monke1.getnumber())

for i in range(1, len(way_to_root) - 1):
    print(way_to_root[i].monke1.getnumber() , way_to_root[i].monke2.getnumber())
    if way_to_root[i].monke1 == way_to_root[i+1]:
        if way_to_root[i].operation == "+":
            solution.append(solution[i-1] - way_to_root[i].monke2.getnumber())
        if way_to_root[i].operation == "-":
            solution.append(solution[i-1] + way_to_root[i].monke2.getnumber())
        if way_to_root[i].operation == "*":
            solution.append(solution[i-1] / way_to_root[i].monke2.getnumber())
        if way_to_root[i].operation == "/":
            solution.append(solution[i-1] * way_to_root[i].monke2.getnumber())
    else:
        if way_to_root[i].operation == "+":
            solution.append(solution[i-1] - way_to_root[i].monke1.getnumber())
        if way_to_root[i].operation == "-":
            solution.append(way_to_root[i].monke1.getnumber() - solution[i-1])
        if way_to_root[i].operation == "*":
            solution.append(solution[i-1] / way_to_root[i].monke1.getnumber())
        if way_to_root[i].operation == "/":
            solution.append(way_to_root[i].monke1.getnumber() / solution[i-1])

print(solution)
        



