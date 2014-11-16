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

def mapDraw(screen, currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, moduleNumber):
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
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
    tileTypes = {'grass':',','seed':'.','tree':'t','town':'T','shop':'$','monster':'M','water':'W','fire':'F','newFire':'f','mountain':'M','mine':'m','craftShop':'C','quest':'!','alter':'A','hole':'O'} 
    tileColours = {'grass':16,'seed':3,'tree':3,'town':14,'shop':15,'monster':5,'water':2,'fire':13,'newFire':13,'mountain':16,'mine':7,'craftShop':4,'quest':15,'alter':2,'hole':16}
    screen.addstr(tilePosY, tilePosX, tileTypes[currentTile], curses.color_pair(tileColours[currentTile]))

def mapEvents(currentMap, playerPosX, playerPosY):
    moduleSizeX, moduleSizeY = moduleSize()
    for i in range(moduleSizeY):
        for j in range (moduleSizeX):
            tilePosX = j + playerPosX - int(moduleSizeX/2)
            tilePosY = i + playerPosY - int(moduleSizeY/2)
            currentTile = currentMap[tilePosX][tilePosY]
            if currentTile == 'tree':
                if tileNextTo(currentMap, tilePosX, tilePosY, 'fire'):
                    if not tileNextTo(currentMap, tilePosX, tilePosY, 'water', "none", 2):
                        currentMap[tilePosX][tilePosY] = 'newFire'
            elif currentTile == 'seed':
                if random.randint(1,30) == 1:
                    currentMap[tilePosX][tilePosY] = 'tree'
            elif currentTile == 'newFire':
                if random.randint(1,3) == 1:
                    currentMap[tilePosX][tilePosY] = 'fire'
            elif currentTile == 'fire':
                if random.randint(1,10) == 1:
                    currentMap[tilePosX][tilePosY] = 'grass'
            elif currentTile == 'monster':
                randomMoveSeed = random.randint(-1,1)
                if random.randint(1,2) == 1:
                    if currentMap[tilePosX + randomMoveSeed][tilePosY] == 'grass':
                        currentMap[tilePosX + randomMoveSeed][tilePosY] = 'monster'
                        currentMap[tilePosX][tilePosY] = 'grass'
                    elif currentMap[tilePosX + randomMoveSeed][tilePosY] == 'fire':
                        currentMap[tilePosX + randomMoveSeed][tilePosY] = 'fire'
                        currentMap[tilePosX][tilePosY] = 'grass'
                elif random.randint(1,2) == 1:
                    if currentMap[tilePosX][tilePosY + randomMoveSeed] == 'grass':
                        currentMap[tilePosX][tilePosY + randomMoveSeed] = 'monster'
                        currentMap[tilePosX][tilePosY] = 'grass'
                    elif currentMap[tilePosX][tilePosY + randomMoveSeed] == 'fire':
                        currentMap[tilePosX][tilePosY + randomMoveSeed] = 'fire'
                        currentMap[tilePosX][tilePosY] = 'grass'
            elif currentTile == 'hole':
                if tileNextTo(currentMap, tilePosX, tilePosY, 'water'):
                    currentMap[tilePosX][tilePosY] = 'water'

    return currentMap

def tileNextTo(currentMap, tilePosX, tilePosY, tileToFind, direction="none", branch=1):
    try:
        if direction == 'none' and branch == 1:
            if tileToFind == currentMap[tilePosX+1][tilePosY]:
                return True
            elif tileToFind == currentMap[tilePosX][tilePosY+1]:
                return True
            elif tileToFind == currentMap[tilePosX-1][tilePosY]:
                return True
            elif tileToFind == currentMap[tilePosX][tilePosY-1]:
                return True
        elif direction == 'none' and branch == 2:
            if tileNextTo(currentMap, tilePosX+1, tilePosY, tileToFind):
                if tileNextTo(currentMap, tilePosX, tilePosY+1, tileToFind):
                    if tileNextTo(currentMap, tilePosX-1, tilePosY, tileToFind):
                        if tileNextTo(currentMap, tilePosX, tilePosY-1, tileToFind):
                            return True
        pass
    except IndexError:
        i = 1 # this does nothing...