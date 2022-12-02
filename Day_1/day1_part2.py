file = open("input.txt" , 'r')
lines = file.readlines()

top1 = 0
top2 = 0
top3 = 0
current = 0

for line in lines:
    if line == "\n":
        if current > top1:
            top3 = top2
            top2 = top1
            top1 = current
        elif current > top2:
            top3 = top2
            top2 = current
        elif current > top3:
            top3 = current
        current = 0
    else:
        current += int(line)
    
file.close()

print(top1 + top2 + top3)