import curses
import random
from inventoryManager import *
from mapManager import *
from actionManager import *
from skillManager import *
from screenManager import *

def main(screen):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)
    screen.nodelay(True)
    screen.clear()
    screenSizeY, screenSizeX = screen.getmaxyx()
    mapSizeX = 1000
    mapSizeY = 1000
    inventoryPosY = mapSizeY + int(mapSizeY/10)
    descriptionBoxX = mapSizeX + int(mapSizeX/10)
    skillManagerDisplayX = descriptionBoxX
    skillManagerDisplayY = inventoryPosY
    playerPosX = 500
    playerPosY = 500
    ax = 0
    ay = 0
    currentMap = mapGenerate(mapSizeX, mapSizeY)
    inventory = []
    skills = {}
    shop = {'logs':2}

    while True:
        screen.clear()
        screenBorders(screen)
        mapDraw(screen, currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY)
        currentMap = actionManagerAction(currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, screen)
        skillManagerDisplay(screen, skills)
        inventoryManager(inventory, screen, inventoryPosY)
        key = screen.getch()
        playerPosX, playerPosY, currentMap, inventory, skills = actionManagerKey(key, 
            playerPosX, playerPosY, currentMap, inventory, skills, screen)

        #playerPosX = max(0,  playerPosX)
        #playerPosX = min(screenSizeX-1, playerPosX)
        #playerPosY = max(0,  playerPosY)
        #playerPosY = min(screenSizeY-1, playerPosY)


if __name__ == '__main__':
    screenSetup()
    curses.wrapper(main)