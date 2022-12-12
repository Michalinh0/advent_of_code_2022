#file = open("input.txt" , 'r')
file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

monkes = list()

class Monke:

    def __init__(self):
        self.number = None
        self.items = None
        self.operation = None
        self.test = None
        self.throw_true = None
        self.throw_false = None
        self.inspected = 0

    def get_n(self):
        return self.number
    
    def get_i(self):
        return self.items
    
    def get_o(self):
        return self.operation
    
    def get_t(self):
        return self.test

    def get_tt(self):
        return self.throw_true

    def get_tf(self):
        return self.throw_false

    def set_n(self , number):
        self.number = number
    
    def set_i(self , items):
        self.items = items
    
    def set_o(self , operation):
        self.operation = operation
    
    def set_t(self , test):
        self.test = test

    def set_tt(self , throw_true):
        self.throw_true = throw_true

    def set_tf(self , throw_false):
        self.throw_false = throw_false

    def get_in(self):
        return self.inspected

    def inspect(self):
        for i in self.items:
            self.inspected += 1
            if(self.operation[0] == "+"):
                i += int(self.operation[1])
            else:
                if(self.operation[1] == "old"):
                    i = i * i
                else:
                    i = i * int(self.operation[1])
            #print(i)
            i = i // 3
            #print(i , i%self.test)
            #print("-----")
            if(i % self.test == 0):
                self.throw(i , self.throw_true)
            else:
                self.throw(i , self.throw_false)
        self.items = list()

    def throw(self , item , address):
        for i in monkes:
            if address == i.get_n():
                i.catch(item)

    def catch(self , item):
        #print(f"Monke {self.number} catching item with worry {item}")
        self.items.append(item)
            



i = 0

temp = list()

for i in range(len(lines)):
    line = lines[i]
    line = line.split(" ")
    #print(line)
    match(i%7):
        case 0:
            monkes.append(Monke())
            monkes[i//7].set_n(i//7)
        case 1:
            temp = list()
            for j in range(2 , len(line)):
                line[j] = line[j].replace("," , "")
                temp.append(int(line[j]))
            monkes[i//7].set_i(temp)
        case 2:
            monkes[i//7].set_o([line[-2] , line[-1]])
        case 3:
            monkes[i//7].set_t(int(line[-1]))
        case 4:
            monkes[i//7].set_tt(int(line[5]))
        case 5:
            monkes[i//7].set_tf(int(line[5]))
        case 6:
            pass

for i in range(len(monkes)):
    print(monkes[i].get_n() , monkes[i].get_i() , monkes[i].get_o() , monkes[i].get_t() , monkes[i].get_tt() , monkes[i].get_tf() , monkes[i].get_in())

for i in range(20):
    for j in monkes:
        j.inspect()

for i in monkes:
    print(i.get_in())