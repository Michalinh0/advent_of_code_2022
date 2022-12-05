file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

overlap = 0
overlap2 = len(lines)

for line in lines:
    line = line.replace("\n" ,"")
    first, second = line.split(",")
    f1 , f2 = first.split("-")
    s1 , s2 = second.split("-")
    print("f1 = " + str(f1))
    print("f2 = " + str(f2))
    print("s1 = " + str(s1))
    print("s2 = " + str(s2))
    f = set()
    s = set()
    for i in range(int(f1) , int(f2+1)):
        f.add(i)
    for i in range(int(s1) , int(s2+1)):
        s.add(i)
    print(f.intersection(s))
    if(f.intersection(s) == f):
        overlap += 1
    if(f.intersection(s) == f):
        overlap += 1
    if(f.intersection(s) == set()):
        overlap2 -= 1
    print("------------")

print(overlap)
print(overlap2)
