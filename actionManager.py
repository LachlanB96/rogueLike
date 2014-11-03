import sys
import curses

def actionManagerKey(key, playerPosX, playerPosY, currentMap):
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
        actionManagerAction.chopDownTree()

    elif key == ord('f') and currentMap[playerPosX][playerPosY] == "grass" and itemPresentInInventory("logs", inventory):
        currentMap[playerPosX][playerPosY] = "fire"
        inventory = removeItemFromInventory("logs", inventory)

    return playerPosX, playerPosY

def actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen):
    descriptionBoxX = mapSizeX + int(mapSizeX/10)
    description = currentMap[playerPosX][playerPosY]
    screen.addch(playerPosY, playerPosX, '@', curses.color_pair(12))
    screen.addstr(0, descriptionBoxX, ("(" + str(mapSizeX) + ", " + str(mapSizeY) + ")"))
    screen.addstr(1, descriptionBoxX, ("(" + str(playerPosX) + ", " + str(playerPosY) + ")"))
    screen.addstr(2, descriptionBoxX, (description))
    return currentMap

def actionManagerDescription():
    if currentMap[playerPosX][playerPosY] == "tree":
        screen.addstr(3, descriptionBoxX, ("Press 'c' to chop down tree"), curses.color_pair(3))

def chopDownTree():
    currentMap[playerPosX][playerPosY] = "grass"
    inventory.append("logs")