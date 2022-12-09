file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

count = 0
chars = list()

for line in lines:
    for i in line:
        count += 1
        chars.append(i)
        if(len(chars) == 5):
            chars.pop(0)
        uni = set()
        for j in chars:
            uni.add(j)
        if(len(uni) == 4):
            break

count2 = 0
chars2 = list()
for line in lines:
    for i in line:
        count2 += 1
        chars2.append(i)
        if(len(chars2) == 15):
            chars2.pop(0)
        uni2 = set()
        for j in chars2:
            uni2.add(j)
        print(uni2)
        if(len(uni2) == 14):
            break

print(count , count2)
