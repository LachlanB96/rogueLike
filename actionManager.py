import sys
import curses
from inventoryManager import *
from shopManager import *
from skillManager import *

def actionManagerKey(bodyPosX, key, playerPosX, playerPosY, currentMap, inventory, skills, screen, inventoryPosY):
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
        shopManagerWelcome(inventory, screen, bodyPosX, inventoryPosY)

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "water" and itemPresentInInventory("fishingRod", inventory):
        inventory.append("fish")
        skills = skillManagerExperience(skills, 'fishing', 8)

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "grass" and itemPresentInInventory("logs", inventory):
        currentMap[playerPosX][playerPosY] = "fire"
        inventory = removeItemFromInventory("logs", inventory, 1)
        skills = skillManagerExperience(skills, 'firemaking', 10)

    return playerPosX, playerPosY, currentMap, inventory, skills

def actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen):
    moduleNumber = 2
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    screen.addstr(titlePosY, titlePosX, 'ACTIONS', curses.color_pair(13))
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    description = currentMap[playerPosX][playerPosY]
    screen.addch(playerPosY, playerPosX, '@', curses.color_pair(12))
    screen.addstr(bodyPosY, bodyPosX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
    screen.addstr(bodyPosY + 1, bodyPosX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
    screen.addstr(bodyPosY + 2, bodyPosX, (description))
    if currentMap[playerPosX][playerPosY] == "tree":
        screen.addstr(3, bodyPosX, ("Press 'c' to chop down tree"), curses.color_pair(3))
    elif currentMap[playerPosX][playerPosY] == "monster":
        screen.addstr(3, bodyPosX, ("Press 'a' to attack monster"), curses.color_pair(5))
    elif currentMap[playerPosX][playerPosY] == "shop":
        screen.addstr(3, bodyPosX, ("Press 's' to buy and sell goods"), curses.color_pair(15))
    elif currentMap[playerPosX][playerPosY] == "water":
        screen.addstr(3, bodyPosX, ("Press 'f' to fish"), curses.color_pair(2))
    return currentMap
