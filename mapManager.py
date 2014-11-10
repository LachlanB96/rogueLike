import curses
import random
from screenManager import *

def mapGenerate(mapSizeX, mapSizeY, trees=5, towns=1, shops=2, monsters=4, water=1):
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
    waterRange = range(tilePercentageCounter, tilePercentageCounter + water)
    tilePercentageCounter += water
    for i in range(mapSizeY):
        for j in range (mapSizeX):
            tileSeed = random.randint(0, 100)
            if tileSeed in treeRange: tileType = "tree"
            elif tileSeed in townsRange: tileType = "town"
            elif tileSeed in shopsRange: tileType = "shop"
            elif tileSeed in monstersRange: tileType = "monster"
            elif tileSeed in waterRange: tileType = "water"
            else: tileType = "grass"
            matrix[j][i] = tileType
    return matrix

def mapDraw(screen, currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY):
    titlePosY, titlePosX = screenPositioner(1, "title")
    bodyPosY, bodyPosX = screenPositioner(1, "body")
    screen.addstr(titlePosY, titlePosX, 'MAP', curses.color_pair(13))
    screen.addstr(1, 1, '1', curses.color_pair(3))

    moduleSizeX, moduleSizeY = moduleSize()

    for i in range(moduleSizeY):
        for j in range (moduleSizeX):
            if currentMap[j][i] == "tree": screen.addstr(bodyPosY + i, bodyPosX + j, 't', curses.color_pair(3))
            elif currentMap[j][i] == "town": screen.addstr(bodyPosY + i, bodyPosX + j, 'T', curses.color_pair(14))
            elif currentMap[j][i] == "shop": screen.addstr(bodyPosY + i, bodyPosX + j, '$', curses.color_pair(15))
            elif currentMap[j][i] == "monster": screen.addstr(bodyPosY + i, bodyPosX + j, 'M', curses.color_pair(5))
            elif currentMap[j][i] == "water": screen.addstr(bodyPosY + i, bodyPosX + j, 'W', curses.color_pair(2))
            elif currentMap[j][i] == "fire": screen.addstr(bodyPosY + i, bodyPosX + j, 'F', curses.color_pair(13))
            else: screen.addstr(i, j, ',')