import random
f = open("verbs.txt")
#print (f.read())
verbs = []
for word in f:
    objects.append(word.strip('\n'))
def getRandomWord():
    t = random.randint(0,79)
    x = verbs[t]
    return x

getRandomWord()
