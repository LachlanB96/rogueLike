import sys
import curses
import random
from inventoryManager import *
from shopManager import *
from skillManager import *
from mapManager import *

def actionManagerKey(key, playerPosX, playerPosY, currentMap, inventory, skills, screen, actionDescriptions, mapSizeX, mapSizeY):
    if key in [ord('q'), ord('Q')]:
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


    elif key == ord('c') and currentMap[playerPosX][playerPosY] == "tree" and itemPresentInInventory("axe", inventory):
        if random.randint(1,2) == 1:
            inventory.append("seeds")
        currentMap[playerPosX][playerPosY] = "grass"
        inventory.append("logs")
        skills = skillManagerExperience(skills, 'woodcutting', 10)

    elif key == ord('p') and currentMap[playerPosX][playerPosY] == "grass" and itemPresentInInventory("seeds", inventory):
        currentMap[playerPosX][playerPosY] = "seed"
        skills = skillManagerExperience(skills, 'farming', 23)

    elif key == ord('a') and currentMap[playerPosX][playerPosY] == "monster":
        currentMap[playerPosX][playerPosY] = "tree"
        inventory.append("gold")
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

    return playerPosX, playerPosY, currentMap, inventory, skills

def actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen, actionDescriptions):
    moduleNumber = 2
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    screen.addstr(titlePosY, titlePosX, 'ACTIONS', curses.color_pair(13))
    description = currentMap[playerPosX][playerPosY]
    screen.addstr(bodyPosY, bodyPosX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
    screen.addstr(bodyPosY + 1, bodyPosX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
    screen.addstr(bodyPosY + 2, bodyPosX, (description))
    currentTile = currentMap[playerPosX][playerPosY]
    if currentTile in actionDescriptions:
        screen.addstr(bodyPosY, bodyPosX, actionDescriptions[currentTile][0], curses.color_pair(actionDescriptions[currentTile][2]))
    return currentMap