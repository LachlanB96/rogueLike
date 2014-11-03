import curses
import random
from inventory import *
from mapManager import *
from actionManager import *

def mapGenerate(mapSizeX, mapSizeY, trees=5, towns=1, shops=2, monsters=4):
    matrix = [[0 for i in range(mapSizeY)] for i in range(mapSizeX)]
    tilePercentageCounter = 0 #used to track what percent of tiles is taken
    treeRange = range(tilePercentageCounter, trees)
    tilePercentageCounter += trees
    townsRange = range(tilePercentageCounter, tilePercentageCounter + towns)
    tilePercentageCounter += towns
    shopsRange = range(tilePercentageCounter, tilePercentageCounter + shops)
    tilePercentageCounter += shops
    monstersRange = range(tilePercentageCounter, tilePercentageCounter + monsters)
    tilePercentageCounter += monsters
    for i in range(mapSizeY):
        for j in range (mapSizeX):
            tileSeed = random.randint(0, 100)
            if tileSeed in treeRange: tileType = "tree"
            elif tileSeed in townsRange: tileType = "town"
            elif tileSeed in shopsRange: tileType = "shop"
            elif tileSeed in monstersRange: tileType = "monster"
            else: tileType = "grass"
            matrix[j][i] = tileType
    return matrix





def main(screen):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)
    screen.nodelay(True)
    screen.clear()
    screenSizeY, screenSizeX = screen.getmaxyx()
    mapSizeX = int(screenSizeX/2)
    mapSizeY = screenSizeY - int(screenSizeY/2)
    inventoryPosY = mapSizeY + int(mapSizeY/10)
    playerPosX = int(mapSizeX/2)
    playerPosY = int(mapSizeY/2)
    ax = 0
    ay = 0
    currentMap = mapGenerate(mapSizeX, mapSizeY)
    inventory = []

    while True:
        screen.clear()
        for i in range(mapSizeY - 1):
            for j in range (mapSizeX - 1):
                if currentMap[j][i] == "tree": screen.addstr(i, j, 't', curses.color_pair(3))
                elif currentMap[j][i] == "town": screen.addstr(i, j, 'T', curses.color_pair(14))
                elif currentMap[j][i] == "shop": screen.addstr(i, j, '$', curses.color_pair(15))
                elif currentMap[j][i] == "monster": screen.addstr(i, j, 'M', curses.color_pair(5))
                elif currentMap[j][i] == "fire": screen.addstr(i, j, 'F', curses.color_pair(13))
                else: screen.addstr(i, j, ',')
        currentMap = actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen)
        inventoryManager(inventory, screen, inventoryPosY)
        key = screen.getch()
        playerPosX, playerPosY = actionManagerKey(key, playerPosX, playerPosY, currentMap)

        playerPosX = max(0,  playerPosX)
        playerPosX = min(screenSizeX-1, playerPosX)
        playerPosY = max(0,  playerPosY)
        playerPosY = min(screenSizeY-1, playerPosY)


if __name__ == '__main__':
    curses.wrapper(main)