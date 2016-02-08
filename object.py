import random
f = open("objects.txt")
#print (f.read())
objects = []
for word in f:
    objects.append(word.strip('\n'))
def getRandomWord():
    t = random.randint(0, len(objects)-1)
    x = objects[t]
    return x
getRandomWord()
