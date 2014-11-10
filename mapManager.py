import curses
import random
from screenManager import *

def mapGenerate(mapSizeX, mapSizeY, trees=5, towns=1, shops=2, monsters=4, water=1, mountains=1, mine=1, alter=1, craftShop=2):
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
    mountainRange = range(tilePercentageCounter, tilePercentageCounter + mountains)
    tilePercentageCounter += mountains
    mineRange = range(tilePercentageCounter, tilePercentageCounter + mine)
    tilePercentageCounter += mine
    alterRange = range(tilePercentageCounter, tilePercentageCounter + alter)
    tilePercentageCounter += alter
    craftShopRange = range(tilePercentageCounter, tilePercentageCounter + craftShop)
    tilePercentageCounter += craftShop
    for i in range(mapSizeY):
        for j in range (mapSizeX):
            tileSeed = random.randint(0, 100)
            if tileSeed in treeRange: tileType = "tree"
            elif tileSeed in townsRange: tileType = "town"
            elif tileSeed in shopsRange: tileType = "shop"
            elif tileSeed in monstersRange: tileType = "monster"
            elif tileSeed in waterRange: tileType = "water"
            elif tileSeed in mountainRange: tileType = "mountain"
            elif tileSeed in mineRange: tileType = "mine"
            elif tileSeed in alterRange: tileType = "alter"
            elif tileSeed in craftShopRange: tileType = "craftShop"
            else: tileType = "grass"
            matrix[j][i] = tileType
    return matrix

def mapDraw(screen, currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY):
    titlePosY, titlePosX = screenPositioner(1, "title")
    bodyPosY, bodyPosX = screenPositioner(1, "body")
    moduleSizeX, moduleSizeY = moduleSize()
    screen.addstr(titlePosY, titlePosX, 'MAP', curses.color_pair(13))
    screen.addstr(1, 1, '1', curses.color_pair(3))
    for i in range(moduleSizeY):
        for j in range (moduleSizeX):
            tilePosY = bodyPosY + i
            tilePosX = bodyPosX + j
            currentTile = currentMap[j + playerPosX - int(moduleSizeX/2)][i + playerPosY - int(moduleSizeY/2)]
            drawMapTile(currentTile, tilePosY, tilePosX, screen)
    screen.addch(bodyPosY + int(moduleSizeY/2), bodyPosX + int(moduleSizeX/2), '@', curses.color_pair(12))

def drawMapTile(currentTile, tilePosY, tilePosX, screen):
    tileTypes = {'grass':',','tree':'t','town':'T','shop':'$','monster':'M','water':'W','fire':'F','mountain':'M','mine':'m','craftShop':'C','quest':'!','alter':'A'} 
    tileColours = {'grass':16,'tree':3,'town':14,'shop':15,'monster':5,'water':2,'fire':13,'mountain':16,'mine':7,'craftShop':4,'quest':15,'alter':2}
    screen.addstr(tilePosY, tilePosX, tileTypes[currentTile], curses.color_pair(tileColours[currentTile]))