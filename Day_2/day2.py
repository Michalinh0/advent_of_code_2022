file = open("input.txt" , 'r')
#file = open("test.txt" , 'r')
lines = file.readlines()

curr = 0

scores = {
    'rock':1,
    'paper':2,
    'scissors':3
}

outcome = {
    'lose':0,
    'draw':3,
    'win':6
}

curr = 0

for line in lines:
    line = line.replace("\n" , "")
    opp , resp = line.split(" ")
    if(opp == 'A'):
        if(resp == 'X'):
            curr +=(scores.get('rock') + outcome.get('draw'))
        if(resp == 'Y'):
            curr +=(scores.get('paper') + outcome.get('win'))
        if(resp == 'Z'):
            curr +=(scores.get('scissors') + outcome.get('lose'))
    if(opp == 'B'):
        if(resp == 'X'):
            curr +=(scores.get('rock') + outcome.get('lose'))
        if(resp == 'Y'):
            curr +=(scores.get('paper') + outcome.get('draw'))
        if(resp == 'Z'):
            curr +=(scores.get('scissors') + outcome.get('win'))
    if(opp == 'C'):
        if(resp == 'X'):
            curr +=(scores.get('rock') + outcome.get('win'))
        if(resp == 'Y'):
            curr +=(scores.get('paper') + outcome.get('lose'))
        if(resp == 'Z'):
            curr +=(scores.get('scissors') + outcome.get('draw'))

print(curr)
curr = 0

for line in lines:
    line = line.replace("\n" , "")
    opp , resp = line.split(" ")
    if(opp == 'A'):
        if(resp == 'X'):
            curr += (scores.get('scissors') + outcome.get('lose'))
        if(resp == 'Y'):
            curr += (scores.get('rock') + outcome.get('draw'))
        if(resp == 'Z'):
            curr += (scores.get('paper') + outcome.get('win'))
    if(opp == 'B'):
        if(resp == 'X'):
            curr +=(scores.get('rock') + outcome.get('lose'))
        if(resp == 'Y'):
            curr +=(scores.get('paper') + outcome.get('draw'))
        if(resp == 'Z'):
            curr +=(scores.get('scissors') + outcome.get('win'))
    if(opp == 'C'):
        if(resp == 'X'):
            curr +=(scores.get('paper') + outcome.get('lose'))
        if(resp == 'Y'):
            curr +=(scores.get('scissors') + outcome.get('draw'))
        if(resp == 'Z'):
            curr +=(scores.get('rock') + outcome.get('win'))

print(curr)

