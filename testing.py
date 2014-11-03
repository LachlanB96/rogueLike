foo=input('Enter a file name: ')
skill = int(foo)
level = 1
while skill - 10*2**(level - 1) > -100000:
    print (skill)
    print (level)
    print (" ")
    skill -= 10*2**(level - 1)
    level +=1
print ("exp: " + str(skill) + " || lvl: " + str(level))