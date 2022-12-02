file = open("input.txt" , 'r')
lines = file.readlines()

maximum = 0
current = 0

for line in lines:
    if line == "\n":
        if current > maximum:
            maximum = current
        current = 0
    else:
        current += int(line)

file.close()
    
print(maximum)
