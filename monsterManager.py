import random

class Monster():
    def __init__(self, positionX, positionY):
        self.posX = positionX
        self.posY = positionY
        continants = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        vowel = ['a','e','i','o','u']
        descriptives = ['snarky', 'fierce', 'ugly', 'possessed', 'bloody', 'gruesome', 'beautiful']
        bodyParts = ['eye', 'mouth', 'torso', 'spikes', 'arms']
        self.level = random.randint(1,10)
        self.name = ""
        self.bodyPart = ""
        self.health = 250
        for i in range(random.randint(1,2)):
            self.name += continants[random.randint(1,len(continants)-1)]
            self.name += vowel[random.randint(0,len(vowel)-1)]
            if random.randint(1,3) == 1:
                self.name += vowel[random.randint(0,len(vowel)-1)]
            self.name += continants[random.randint(0,len(continants)-1)]
        self.bodyPart = descriptives[random.randint(0,len(descriptives)-1)] + " " + bodyParts[random.randint(0,len(bodyParts)-1)]

    def posAt(self, posX, posY):
        if self.posX == posX and self.posY == posY:
            return True
        else:
            return False

    def update(self, currentMap, tilePosX, tilePosY):
        randomMoveSeed = random.randint(-1,1)
        if random.randint(1,2) == 1:
            if currentMap[tilePosX + randomMoveSeed][tilePosY] == 'grass':
                currentMap[tilePosX + randomMoveSeed][tilePosY] = 'monster'
                currentMap[tilePosX][tilePosY] = 'grass'
                self.posX += randomMoveSeed
            elif currentMap[tilePosX + randomMoveSeed][tilePosY] == 'fire':
                currentMap[tilePosX + randomMoveSeed][tilePosY] = 'fire'
                currentMap[tilePosX][tilePosY] = 'grass'
                self.posX -= randomMoveSeed
        elif random.randint(1,2) == 1:
            if currentMap[tilePosX][tilePosY + randomMoveSeed] == 'grass':
                currentMap[tilePosX][tilePosY + randomMoveSeed] = 'monster'
                currentMap[tilePosX][tilePosY] = 'grass'
                self.posY += randomMoveSeed
            elif currentMap[tilePosX][tilePosY + randomMoveSeed] == 'fire':
                currentMap[tilePosX][tilePosY + randomMoveSeed] = 'fire'
                currentMap[tilePosX][tilePosY] = 'grass'
                self.posY -= randomMoveSeed
        return currentMap

    def description(self):
        return self.name + " has (a) " + self.bodyPart + " and is level " + str(self.level) + " with " + str(self.health) + " health."
