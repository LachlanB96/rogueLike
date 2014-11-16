import sys
import curses
import random
from inventoryManager import *
from shopManager import *
from skillManager import *
from mapManager import *
from screenManager import *
from questManager import *

def actionManagerKey(playerPosX, playerPosY, currentMap, inventory, skills, screen, actionDescriptions, mapSizeX, mapSizeY, activeQuests, modulePositions, textToDisplay):
    textToDisplay = []
    key = screen.getch()
    if key == ord('Q'):
        sys.quit()
    if key == curses.KEY_LEFT:
        playerPosX = playerPosX - 1
        currentMap = mapEvents(currentMap, playerPosX, playerPosY)
    elif key == curses.KEY_RIGHT:
        playerPosX = playerPosX + 1
        currentMap = mapEvents(currentMap, playerPosX, playerPosY)
    elif key == curses.KEY_UP:
        playerPosY = playerPosY - 1
        currentMap = mapEvents(currentMap, playerPosX, playerPosY)
    elif key == curses.KEY_DOWN:
        playerPosY = playerPosY + 1
        currentMap = mapEvents(currentMap, playerPosX, playerPosY)

    elif key == ord('1') or key == ord('2') or key == ord('3') or key == ord('4'):
        modulePositions = moduleReposition(key, modulePositions, screen)

    elif key == ord('w'):
        currentMap = mapEvents(currentMap, playerPosX, playerPosY)



    if currentMap[playerPosX][playerPosY] == "grass":
        if itemPresentInInventory("seeds", inventory):
            if tileNextTo(currentMap, playerPosX, playerPosY, 'water'):
                textToDisplay.append(("Press 'p' to plant seed" , 16))
                if key == ord('p'):
                    currentMap[playerPosX][playerPosY] = "seed"
                    skills = skillManagerExperience(skills, 'farming', 23)
        if itemPresentInInventory("shovel", inventory):
            textToDisplay.append(("Press 'd' to dig a hole" , 16))
            if key == ord('d'):
                currentMap[playerPosX][playerPosY] = "hole"
                skills = skillManagerExperience(skills, 'strength', 2)

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

    elif currentMap[playerPosX][playerPosY] == "quest":
        for quest in activeQuests:
            if quest[1] == str(playerPosX) + "," + str(playerPosY):
                if key == ord('q'):
                    updatedQuest = (quest[0],quest[1],"return",quest[3],quest[4])
                    activeQuests.remove(quest)
                    activeQuests.append(updatedQuest)
                    currentMap[playerPosX][playerPosY] = "grass"

    elif key == ord('a') and currentMap[playerPosX][playerPosY] == "monster":
        inventory.append("gold")
        currentMap[playerPosX][playerPosY] = "grass"
        skills = skillManagerExperience(skills, 'attack', 10)

    elif key == ord('s') and currentMap[playerPosX][playerPosY] == "shop":
        shopManagerManager(inventory, screen)

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "water" and itemPresentInInventory("fishingRod", inventory):
        inventory.append("fish")
        inventory = removeItemFromInventory("fishingRod", inventory, 1)
        skills = skillManagerExperience(skills, 'fishing', 8)

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "grass" and itemPresentInInventory("logs", inventory):
        currentMap[playerPosX][playerPosY] = "fire"
        inventory = removeItemFromInventory("logs", inventory, 1)
        skills = skillManagerExperience(skills, 'firemaking', 10)

    return playerPosX, playerPosY, currentMap, inventory, skills, activeQuests, modulePositions, textToDisplay

def actionManagerDisplay(screen, moduleNumber, textToDisplay, currentMap, mapSizeX, mapSizeY, playerPosX, playerPosY):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'ACTIONS', curses.color_pair(13))
        description = currentMap[playerPosX][playerPosY]
        screen.addstr(bodyPosY, bodyPosX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
        screen.addstr(bodyPosY + 1, bodyPosX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
        screen.addstr(bodyPosY + 2, bodyPosX, (description))
        i = 0
        for line in textToDisplay:
            screen.addstr(bodyPosY + 3 + i, bodyPosX, line[0], curses.color_pair(line[1]))
            i += 1