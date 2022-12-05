file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

front = set()
back = set()

print(ord('p') - 96)

curr = 0
mod = 0

for line in lines:
    line = line.replace("\n" ,"")
    left = 0
    right = len(line)-1
    front = set()
    back = set()
    while(left < right):
        front.add(line[left])
        back.add(line[right])
        left +=1
        right -= 1
    inter = front.intersection(back)
    print(inter)
    for i in inter:
        if(ord(i) < 97):
            curr += (ord(i) - 38)
            print("Big")
        else:
            curr += (ord(i) - 96)
            print("Smol")

print(curr)
