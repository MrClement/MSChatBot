import random
f = open("objects.txt")
objects = []
for word in f:
    objects.append(word.strip('\n'))
def getRandomWord():
    t = random.randint(0, 64)
    x = objects[t]
    return x
