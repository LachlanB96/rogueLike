import random

for i in range(20):
    continants = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    vowel = ['a','e','i','o','u']
    name = ""
    for i in range(random.randint(1,2)):
        name += continants[random.randint(1,len(continants)-1)]
        name += vowel[random.randint(1,len(vowel)-1)]
        if random.randint(1,2) == 1:
            name += vowel[random.randint(1,len(vowel)-1)]
        name += continants[random.randint(1,len(continants)-1)]
    print (name)