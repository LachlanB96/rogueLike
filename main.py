import curses
import random
from inventoryManager import *
from mapManager import *
from actionManager import *
from skillManager import *
from screenManager import *
from questManager import *

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
    modulePositions = {'map':1,'actions':2,'inventory':3,'skills':4, 'quests':5}
    inventory = ['axe', 'shovel']
    skills = {}
    #quest tuple is (<townCoord>,<questCoord>,<questType>,<rewardType>,<reward>)
    activeQuests = []
    shop = {'logs':2}
    actionDescriptions = {'grass':(("Press 'p' to plant seed"), 16), 
        'tree':(("Press 'c' to chop down tree"), 3),
        'town':(("Press 'e' to enter town"), 14), 
        'shop':(("Press 's' to enter shop"), 15),
        'monster':(("Press 'a' to attack monster"), 5), 
        'water':(("Press 'f' to fish the water"), 2),
        'fire':(("Press 'f' to start fire"), 13), 
        'mountain':(("Press 'e' to explore mountain"), 16),
        'mine':(("Press 'm' to mine ore"), 7), 
        'craftShop':(("Press 'c' to enter shop"), 4),
        'quest':(("Press 'e' to complete quest"), 15), 
        'alter':(("Press 'p' to pray"), 2),
        }
    textToDisplay = [("Test",13),("another test!",5)]

    while True:
        screen.clear()
        screenBorders(screen)
        mapDraw(screen, currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, modulePositions['map'])
        skillManagerDisplay(screen, skills, modulePositions['skills'])
        inventoryManager(inventory, screen, inventoryPosY, modulePositions['inventory'])
        questManagerDisplay(screen, activeQuests, modulePositions['quests'])
        actionManagerDisplay(screen, modulePositions['actions'], textToDisplay, currentMap, mapSizeX, mapSizeY, playerPosX, playerPosY)
        playerPosX, playerPosY, currentMap, inventory, skills, activeQuests, modulePositions, textToDisplay = actionManagerKey(playerPosX, playerPosY, currentMap, inventory, skills, screen, actionDescriptions, mapSizeX, mapSizeY, activeQuests, modulePositions, textToDisplay)

        #playerPosX = max(0,  playerPosX)
        #playerPosX = min(screenSizeX-1, playerPosX)
        #playerPosY = max(0,  playerPosY)
        #playerPosY = min(screenSizeY-1, playerPosY)


if __name__ == '__main__':
    screenSetup()
    curses.wrapper(main)