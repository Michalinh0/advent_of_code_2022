file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

unique = set()
banned = set()

constant = 2000000

for line in lines:
    l = []
    for t in line.split():
        t = t.replace("," , "")
        t = t.replace(":" , "")
        if(t[-1].isdigit()):
            t = t.replace("x=" , "")
            t = t.replace("y=" , "")
            l.append(int(t))
    if(l[3] == constant):
        #print("Banning " + str(l[2]))
        banned.add(l[2])
    xdist = abs(l[0] - l[2])
    ydist = abs(l[1] - l[3])
    dist = xdist + ydist
    #print(l , xdist , ydist , dist)
    if(l[1] < constant):
        if(l[1] + dist >= constant):
            offset = l[1] + dist - constant
            for i in range(l[0] - offset , l[0] + offset + 1):
                unique.add(i)
    elif(l[1] > constant):
        if(l[1] - dist <= constant):
            offset = abs(l[1] - dist - constant)
            for i in range(l[0] - offset , l[0] + offset + 1):
                unique.add(i)
    else:
        offset = dist
        for i in range(l[0] - offset , l[0] + offset + 1):
                unique.add(i)


unique = unique.difference(banned)
print(len(unique))
# Part 2

borderpoints = set()
sensors = list()

for line in lines:
    l = []
    for t in line.split():
        t = t.replace("," , "")
        t = t.replace(":" , "")
        if(t[-1].isdigit()):
            t = t.replace("x=" , "")
            t = t.replace("y=" , "")
            l.append(int(t))
    xdist = abs(l[0] - l[2])
    ydist = abs(l[1] - l[3])
    dist = xdist + ydist
    sensors.append((l[0] , l[1] , dist))
    for i in range(dist):
        borderpoints.add((l[0]-dist-1+i , l[1]-i))
        borderpoints.add((l[0]+i , l[1]-dist-1+i))
        borderpoints.add((l[0]+dist+1-i , l[1]+i))
        borderpoints.add((l[0]-i , l[1]+dist+1-i))
    print("Appended sensor number " , len(sensors))

print("Points to compute : " , len(borderpoints))

i = 0

for point in borderpoints:
    if(point[0] < 0 or point[0] >= 4000000):
        i+=1
        if i%1000 == 0:
            print("Computed" , i , "points")
        continue
    if(point[1] < 0 or point[1] >= 4000000):
        i+=1
        if i%1000 == 0:
            print("Computed" , i , "points")
        continue
    beacon = True
    for sensor in sensors:
        distance = abs(point[0] - sensor[0]) + abs(point[1] - sensor[1])
        if(distance <= sensor[2]):
            beacon = False
            break
    if(beacon):
        print(point)
        break
    i+=1
    if i%1000 == 0:
        print("Computed" , i , "points")


    


