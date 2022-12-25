#file = open("input.txt" , 'r')
file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

left = list()
right = list()

def parse_input(target , input):
    ready = list()
    stack = list()
    i = 0
    for i in range(len(input)):
        if input[i] == "[":
            stack.append(list())
        elif input[i] == "]":
            if(len(stack) > 1):
                stack[-2].append(stack[-1])
            else:
                ready.append(stack[-1])
            stack.pop()
        elif input[i] == "1" and input[i+1] == "0":
            stack[-1].append(10)
        elif 48 <= ord(input[i]) <= 57:
            stack[-1].append(int(input[i]))
    target.append(ready)

def compare(l , r):
    print(l , r , len(l) , len(r))
    for i in range (len(l)):
        if(i == len(r)):
            return True
        if isinstance(l[i] , int) and isinstance(r[i] , int):
            if(l[i] > r[i]):
                return False
            else:
                return True
        if isinstance(l[i] , list) and isinstance(r[i] , list):
            return compare(l[i] , r[i])
        if isinstance(l[i] , int) and isinstance(r[i] , list):
            temp = [l[i]]
            return compare(temp , r[i])
        if isinstance(l[i] , list) and isinstance(r[i] , int):
            temp = [l[i]]
            return compare(l[i] , temp)
        if(i + 1 == len(l) and len(r) > len(l)):
            return False


mod = 0
for i in lines:
    if mod % 3 == 0:
        parse_input(left , i)
    if mod % 3 == 1:
        parse_input(right , i)
    mod += 1


i = 0
count = 0

compare(left[1] , right[1])


for i in range(len(left)):
    if compare(left[i] , right[i]):
        count += i + 1
    print(count)

print(count)

