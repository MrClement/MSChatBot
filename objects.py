import random
f = open("objects.txt")
#print (f.read())
objects = []
for word in f:
    objects.append(word.strip('\n'))
print objects
