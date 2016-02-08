import random
file = open("subjects.txt","r")
x = []
file.readline()
for line in file:
    x.append(line.strip('\n'))

def getRandomWord():
    o = len(x)-1
    rand = random.randint(0, o)
    return x[rand]
