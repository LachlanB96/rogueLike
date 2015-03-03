import curses
import random
from screenManager import *
from monsterManager import *
from townManager import *

def mapGenerate(mapSizeX, mapSizeY, trees=500, towns=1000, shops=200, monsters=400, water=100, mountains=100, mine=100, alter=100, craftShop=200):
    monstersList = []
    townsList = []
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
            tileSeed = random.randint(0, 10000)
            if tileSeed in treeRange: tileType = "tree"
            elif tileSeed in townsRange: tileType = "town"
            elif tileSeed in shopsRange: tileType = "shop"
            elif tileSeed in monstersRange:
                tileType = "monster"
                monster = Monster(j, i)
                monstersList.append(monster)
            elif tileSeed in waterRange: tileType = "water"
            elif tileSeed in mountainRange: tileType = "mountain"
            elif tileSeed in mineRange: tileType = "mine"
            elif tileSeed in alterRange: tileType = "alter"
            elif tileSeed in craftShopRange: tileType = "craftShop"
            else: tileType = "grass"
            matrix[j][i] = tileType
    for i in range(mapSizeY):
        for j in range (mapSizeX):
            size = random.randint(3,15)
            if tileNearEdge(mapSizeX, mapSizeY, j, i) > size*2+1:
                if matrix[j][i] == "town":
                    if not tileNextTo(matrix, j, i, 'townWall', size*2):
                        matrix, townsList = townGenerate(matrix, j, i, size, townsList)
                    else:
                        matrix[j][i] = 'grass'

    return matrix, monstersList, townList

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
    tileTypes = {'grass':',','seed':'.','tree':'t','town':'T','shop':'$','monster':'M','water':'W',
    'fire':'F','newFire':'f','mountain':'M','mine':'m','craftShop':'C','quest':'!','alter':'A',
    'hole':'O','corruptSeed':'.','townWall':'H'} 
    tileColours = {'grass':16,'seed':3,'tree':3,'town':14,'shop':15,'monster':5,'water':2,
    'fire':13,'newFire':13,'mountain':16,'mine':7,'craftShop':4,'quest':15,'alter':2,
    'hole':16,'corruptSeed':3,'townWall':16}
    screen.addstr(tilePosY, tilePosX, tileTypes[currentTile], curses.color_pair(tileColours[currentTile]))

def mapEvents(currentMap, playerPosX, playerPosY, monsters):
    moduleSizeX, moduleSizeY = moduleSize()
    for i in range(moduleSizeY):
        for j in range (moduleSizeX):
            tilePosX = j + playerPosX - int(moduleSizeX/2)
            tilePosY = i + playerPosY - int(moduleSizeY/2)
            currentTile = currentMap[tilePosX][tilePosY]
            if currentTile == 'tree':
                if tileNextTo(currentMap, tilePosX, tilePosY, 'fire'):
                    if not tileNextTo(currentMap, tilePosX, tilePosY, 'water', 2):
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
                for monster in monsters:
                    if monster.posAt(tilePosX, tilePosY):
                        currentMap = monster.update(currentMap,tilePosX, tilePosY)
            elif currentTile == 'hole':
                if tileNextTo(currentMap, tilePosX, tilePosY, 'water'):
                    currentMap[tilePosX][tilePosY] = 'water'

    return currentMap

def tileNextTo(currentMap, tilePosX, tilePosY, tileToFind, branch=1, direction="none"):
    try:
        branch += 1
        if direction == "none":
            for i in range(branch+1):
                for j in range(i):
                    if currentMap[tilePosX-branch+i][tilePosY+j] == tileToFind:
                        return True
                    if currentMap[tilePosX-branch+i][tilePosY-j] == tileToFind:
                        return True
                    if currentMap[tilePosX+branch-i][tilePosY+j] == tileToFind:
                        return True
                    if currentMap[tilePosX+branch-i][tilePosY-j] == tileToFind:
                        return True
            return False
        pass
    except IndexError:
        i = 1 # this does nothing...

def tileNearEdge(mapSizeX, mapSizeY, posX, posY):
    distanceFromEdge = 500
    if posX < distanceFromEdge: distanceFromEdge = posX
    if mapSizeX - posX < distanceFromEdge: distanceFromEdge = mapSizeX - posX
    if posY < distanceFromEdge: distanceFromEdge = posY
    if mapSizeY - posY < distanceFromEdge: distanceFromEdge = mapSizeY - posY
    return distanceFromEdge

def changeTile(currentMap, tilePosX, tilePosY, newTile, branch=1, pattern="plus"):
    if pattern == "plus":
        for i in range(0,branch+1):
            for j in range(0,i):
                currentMap[tilePosX-branch+i][tilePosY+j] = newTile
                currentMap[tilePosX-branch+i][tilePosY-j] = newTile
                currentMap[tilePosX+branch-i][tilePosY+j] = newTile
                currentMap[tilePosX+branch-i][tilePosY-j] = newTile


    return currentMap