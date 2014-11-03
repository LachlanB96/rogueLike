import sys
import curses
from inventoryManager import *

def actionManagerKey(key, playerPosX, playerPosY, currentMap, inventory):
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

    elif key == ord('c') and currentMap[playerPosX][playerPosY] == "tree":
        currentMap[playerPosX][playerPosY] = "grass"
        inventory.append("logs")

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "grass" and itemPresentInInventory("logs", inventory):
        currentMap[playerPosX][playerPosY] = "fire"
        inventory = removeItemFromInventory("logs", inventory)

    return playerPosX, playerPosY, currentMap, inventory

def actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen):
    descriptionBoxX = mapSizeX + int(mapSizeX/10)
    description = currentMap[playerPosX][playerPosY]
    screen.addch(playerPosY, playerPosX, '@', curses.color_pair(12))
    screen.addstr(0, descriptionBoxX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
    screen.addstr(1, descriptionBoxX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
    screen.addstr(2, descriptionBoxX, (description))
    if currentMap[playerPosX][playerPosY] == "tree":
        screen.addstr(3, descriptionBoxX, ("Press 'c' to chop down tree"), curses.color_pair(3))
    return currentMap
