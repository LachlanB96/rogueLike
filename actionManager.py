import sys
import curses
from inventoryManager import *
from shopManager import *
from skillManager import *

def actionManagerKey(key, playerPosX, playerPosY, currentMap, inventory, skills, screen):
    if key in [ord('q'), ord('Q')]:
        sys.quit()
    if key == curses.KEY_LEFT:
        playerPosX = playerPosX - 1
    elif key == curses.KEY_RIGHT:
        playerPosX = playerPosX + 1
    elif key == curses.KEY_UP:
        playerPosY = playerPosY - 1
    elif key == curses.KEY_DOWN:
        playerPosY = playerPosY + 1

    elif key == ord('c') and currentMap[playerPosX][playerPosY] == "tree" and itemPresentInInventory("axe", inventory):
        currentMap[playerPosX][playerPosY] = "grass"
        inventory.append("logs")
        skills = skillManagerExperience(skills, 'woodcutting', 10)

    elif key == ord('a') and currentMap[playerPosX][playerPosY] == "monster":
        currentMap[playerPosX][playerPosY] = "tree"
        inventory.append("gold")
        skills = skillManagerExperience(skills, 'attack', 10)

    elif key == ord('s') and currentMap[playerPosX][playerPosY] == "shop":
        shopManagerWelcome(inventory, screen)

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "water" and itemPresentInInventory("fishingRod", inventory):
        inventory.append("fish")
        inventory = removeItemFromInventory("fishingRod", inventory, 1)
        skills = skillManagerExperience(skills, 'fishing', 8)

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "grass" and itemPresentInInventory("logs", inventory):
        currentMap[playerPosX][playerPosY] = "fire"
        inventory = removeItemFromInventory("logs", inventory, 1)
        skills = skillManagerExperience(skills, 'firemaking', 10)

    return playerPosX, playerPosY, currentMap, inventory, skills

def actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen):
    moduleNumber = 2
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    screen.addstr(titlePosY, titlePosX, 'ACTIONS', curses.color_pair(13))
    description = currentMap[playerPosX][playerPosY]
    screen.addstr(bodyPosY, bodyPosX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
    screen.addstr(bodyPosY + 1, bodyPosX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
    screen.addstr(bodyPosY + 2, bodyPosX, (description))
    currentTile = currentMap[playerPosX][playerPosY]
    actionDescriptions = {'grass':("Press 'p' to plant seed", 'p', 16), 
        'tree':("Press 'c' to chop down tree", 'c', 3),
        'town':("Press 'e' to enter town", 'e', 14), 
        'shop':("Press 's' to enter shop", 's', 15),
        'monster':("Press 'a' to attack monster", 'a', 5), 
        'water':("Press 'f' to fish the water", 'f', 2),
        'fire':("Press 'f' to start fire", 'f', 13), 
        'mountain':("Press 'e' to explore mountain", 'e', 16),
        'mine':("Press 'm' to mine ore", 'm', 7), 
        'craftShop':("Press 'c' to enter shop", 'c', 4),
        'quest':("Press 'q' to complete quest", 'q', 15), 
        'alter':("Press 'p' to pray", 'p', 2),
        }
    if currentTile in actionDescriptions:
        screen.addstr(bodyPosY, bodyPosX, actionDescriptions[currentTile][0], curses.color_pair(actionDescriptions[currentTile][2]))
    return currentMap