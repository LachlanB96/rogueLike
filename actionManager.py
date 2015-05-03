import sys
import curses
import random
from inventoryManager import *
from shopManager import *
from skillManager import *
from mapManager import *
from screenManager import *
from questManager import *

def actionManagerKey(currentMap, playerPosX, playerPosY, inventory, skills, screen, activeQuests, modulePositions, textToDisplay, prayerPoints):
    textToDisplay = []
    key = screen.getch()
    playerMoveDirection = ('x','y')
    if not key == -1: 
        if key == ord('Q'):
            sys.quit()

        if key == curses.KEY_LEFT:
            playerMoveDirection = (-1,0)
        elif key == curses.KEY_RIGHT:
            playerMoveDirection = (1,0)
        elif key == curses.KEY_UP:
            playerMoveDirection = (0,-1)
        elif key == curses.KEY_DOWN:
            playerMoveDirection = (0,1)
        elif key == ord('w'):
            playerMoveDirection = (0,0)

        elif chr(key) in '123456789':
            module = chr(key)
            modulePositions = moduleReposition(module, modulePositions, screen)

        if currentMap[playerPosX][playerPosY] == "grass":
            if itemPresentInInventory("seeds", inventory):
                if tileNextTo(currentMap, playerPosX, playerPosY, 'water', 3):
                    textToDisplay.append(("Press 'p' to plant seed" , 16))
                    if key == ord('p'):
                        currentMap[playerPosX][playerPosY] = "seed"
                        skills = skillManagerExperience(skills, 'farming', 23)
            if itemPresentInInventory("shovel", inventory):
                textToDisplay.append(("Press 'd' to dig a hole" , 16))
                if key == ord('d'):
                    if random.randint(1, 5) == 1:
                        inventory.append("bones")
                    currentMap[playerPosX][playerPosY] = "hole"
                    inventory.append("dirt")
                    skills = skillManagerExperience(skills, 'strength', 2)
                    skills = skillManagerExperience(skills, 'terraforming', 10)
                if 'terraforming' in skills:
                    if skillManagerLevel(skills['terraforming']) > 4:
                        textToDisplay.append(("Press 'b' to dig a big hole" , 16))
                        if key == ord('b'):
                            currentMap = changeTile(currentMap, playerPosX, playerPosY, "hole", 2)
                            inventory.append("dirt")
                            skills = skillManagerExperience(skills, 'strength', 2)
                            skills = skillManagerExperience(skills, 'terraforming', 40)
            if itemPresentInInventory("logs", inventory):
                textToDisplay.append(("Press 'f' to start a fire" , 3))
                if key == ord('f'):
                    currentMap[playerPosX][playerPosY] = "fire"
                    inventory = removeItemFromInventory("logs", inventory, 1)
                    skills = skillManagerExperience(skills, 'firemaking', 10)
            if itemPresentInInventory("bones", inventory):
                textToDisplay.append(("Press 'b' to bury bones", 3))
                if key == ord('b'):
                    skills = skillManagerExperience(skills, 'praying', 8)
                    prayerPoints += 10

        elif currentMap[playerPosX][playerPosY] == "seed":
            textToDisplay.append(("Press 't' to trample seed", 3))
            if key == ord('t'):
                currentMap[playerPosX][playerPosY] = "grass"
            if itemPresentInInventory("corrupt dust", inventory):
                textToDisplay.append(("Press 'p' to add corrupt dust to tree", 3))
                if key == ord('p'):
                    currentMap[playerPosX][playerPosY] = "evilSeed"

        elif currentMap[playerPosX][playerPosY] == "tree":
            if itemPresentInInventory("axe", inventory):
                textToDisplay.append(("Press 'c' to chop down tree", 3))
                if key == ord('c'):
                    if random.randint(1, 2) == 1:
                        inventory.append("seeds")
                    currentMap[playerPosX][playerPosY] = "grass"
                    inventory.append("logs")
                    skills = skillManagerExperience(skills, 'woodcutting', 10)

        elif currentMap[playerPosX][playerPosY] == "town":
            textToDisplay.append(("Press 't' to talk", 16))
            textToDisplay.append(("Press 'q' to start a quest", 15))
            if key == ord('q'):
                currentMap, activeQuests = questManagerNew(currentMap, activeQuests, playerPosX, playerPosY)
                skillManagerExperience(skills, 'questing', -25)
            for quest in activeQuests:
                if quest[2] == "return" and quest[0] == str(playerPosX) + "," + str(playerPosY):
                    textToDisplay.append(("Press 'c' to complete quest", 15))
                    if key == ord('c'):
                        for i in range(0,int(quest[4])):
                            inventory.append(quest[3])
                        activeQuests.remove(quest)
                        skillManagerExperience(skills, 'questing', 50)

        elif currentMap[playerPosX][playerPosY] == "shop":
            textToDisplay.append(("Press 's' to shop", 3))
            textToDisplay.append(("Press 'r' to rob shop", 3))
            textToDisplay.append(("Press 'i' to invest in shop", 3))
            if key == ord('s'):
                shopManagerManager(inventory, screen)

        elif currentMap[playerPosX][playerPosY] == "monster":
            textToDisplay.append(("Press 'a' to attack monster", 3))
            textToDisplay.append(("Press 't' to train monster", 3))
            textToDisplay.append(("Press 'f' to flee monster", 3))
            textToDisplay.append(("Press 'd' to defend against monster", 3))
            textToDisplay.append(("Press 'h' to hide from monster", 3))
            if key == ord('a'):
                
                inventory.append("gold")
                currentMap[playerPosX][playerPosY] = "grass"
                skills = skillManagerExperience(skills, 'attack', 10)

        elif currentMap[playerPosX][playerPosY] == "quest":
            for quest in activeQuests:
                if quest[1] == str(playerPosX) + "," + str(playerPosY):
                    if key == ord('q'):
                        updatedQuest = (quest[0],quest[1],"return",quest[3],quest[4])
                        activeQuests.remove(quest)
                        activeQuests.append(updatedQuest)
                        currentMap[playerPosX][playerPosY] = "grass"

        elif currentMap[playerPosX][playerPosY] == "water":
            if itemPresentInInventory("fishingRod", inventory):
                textToDisplay.append(("Press 'f' to fish water", 15))
                if key == ord('f'):
                    inventory.append("fish")
                    inventory = removeItemFromInventory("fishingRod", inventory, 1)
                    skills = skillManagerExperience(skills, 'fishing', 8)
            elif itemPresentInInventory("bucket", inventory):
                textToDisplay.append(("Press 'p' to pickup water", 15))
                if key == ord('p'):
                    inventory.append("water bucket")
                    inventory = removeItemFromInventory("bucket", inventory, 1)
                    currentMap[playerPosX][playerPosY] = "hole"

        elif currentMap[playerPosX][playerPosY] == "hole":
            if itemPresentInInventory("water bucket", inventory):
                textToDisplay.append(("Press 'p' to put down water", 15))
                if key == ord('p'):
                    inventory.append("bucket")
                    inventory = removeItemFromInventory("water bucket", inventory, 1)
                    currentMap[playerPosX][playerPosY] = "water"

        elif currentMap[playerPosX][playerPosY] == "alter":
            if prayerPoints > 15:
                textToDisplay.append(("Press 'w' to pray to the god of staff", 3))
                textToDisplay.append(("Press 's' to pray to the god of sword", 5))
                textToDisplay.append(("Press 'x' to pray to the god of arrow", 10))
                if key == ord('w'):
                    prayerPoints -= 15
                    inventory.append("staff")
                elif key == ord('s'):
                    prayerPoints -= 15
                    inventory.append("sword")
                elif key == ord('x'):
                    prayerPoints -= 15
                    inventory.append("bow")
                    for i in range(10):
                        inventory.append("arrows")


    return currentMap, inventory, skills, activeQuests, modulePositions, textToDisplay, prayerPoints, playerMoveDirection

def actionManagerDisplay(screen, moduleNumber, textToDisplay, currentMap, mapSizeX, mapSizeY, playerPosX, playerPosY, monsters):
    if not moduleNumber == 0:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        bottomPosY, bottomPosX = screenPositioner(moduleNumber, "bottom")
        screen.addstr(titlePosY, titlePosX, 'ACTIONS', curses.color_pair(13))
        description = currentMap[playerPosX][playerPosY]
        screen.addstr(bodyPosY, bodyPosX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
        screen.addstr(bodyPosY + 1, bodyPosX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
        if description == "monster":
            for monster in monsters:
                if monster.posAt(playerPosX, playerPosY):
                    description = monster.description()
        screen.addstr(bodyPosY + 2, bodyPosX, (description))
        i = 0
        for line in textToDisplay:
            screen.addstr(bottomPosY - i, bottomPosX, line[0], curses.color_pair(line[1]))
            i += 1

def playerMovementManager(currentMap, playerPosX, playerPosY, playerMoveDirection):
    if not currentMap[playerPosX+playerMoveDirection[0]][playerPosY+playerMoveDirection[1]] == "townWall":
            playerPosX += playerMoveDirection[0]
            playerPosY += playerMoveDirection[1]
            playerMoved = True
    return playerPosX, playerPosY