import curses
import random
import gspread
from inventoryManager import *
from mapManager import *
from actionManager import *
from skillManager import *
from screenManager import *
from questManager import *
from statManager import *

def main(screen):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)
    screen.nodelay(True)
    screen.clear()
    screenSizeY, screenSizeX = screen.getmaxyx()
    mapSizeX = 300
    mapSizeY = 300
    inventoryPosY = mapSizeY + int(mapSizeY/10)
    descriptionBoxX = mapSizeX + int(mapSizeX/10)
    skillManagerDisplayX = descriptionBoxX
    skillManagerDisplayY = inventoryPosY
    playerPosX = int(mapSizeX/2)
    playerPosY = int(mapSizeY/2)
    ax = 0
    ay = 0
    currentMap, monsters, towns = mapGenerate(mapSizeX, mapSizeY)
    modulePositions = {'map':1,'actions':2,'inventory':3,'skills':5, 'quests':5, 'stats':4}
    inventory = ['axe', 'shovel', 'bucket']
    skills = {}
    prayerPoints = 0
    playerMoveDirection = ('x','y')
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
    # Stats are in order, health, mana, attack, defense, speed, left wield, right wield, head, neck, torso, left arm, right arm, legs, feet, pet
    playerStats = [100, 100, 100, 100, 10, 1, 1, 11, 1, 12, 1, 1, 35, 14, 20]
    textToDisplay = [("Test",13),("another test!",5)]
    armourUpdated = True

    while True:
        screen.clear()
        screenBorders(screen)
        mapDraw(screen, currentMap, playerPosX, playerPosY, mapSizeX, mapSizeY, modulePositions['map'])
        skillManagerDisplay(screen, skills, modulePositions['skills'])
        inventoryManager(inventory, screen, inventoryPosY, modulePositions['inventory'])
        questManagerDisplay(screen, activeQuests, modulePositions['quests'])
        statManagerDisplay(screen, modulePositions['stats'], playerStats, armourUpdated)
        actionManagerDisplay(screen, modulePositions['actions'], textToDisplay, currentMap, mapSizeX, mapSizeY, playerPosX, playerPosY, monsters)
        currentMap, inventory, skills, activeQuests, modulePositions, textToDisplay, prayerPoints, playerMoveDirection = actionManagerKey(currentMap, playerPosX, playerPosY, inventory, skills, screen, activeQuests, modulePositions, textToDisplay, prayerPoints)
        if not playerMoveDirection[0] == 'x' and not playerMoveDirection[1] == 'y':
            playerPosX, playerPosY = playerMovementManager(currentMap, playerPosX, playerPosY, playerMoveDirection)
            currentMap = mapEvents(currentMap, playerPosX, playerPosY, monsters)

        armourUpdated = False #this is just for optimaiation so the spreadsheet isn't queried a billion times a second
        #playerPosX = max(0,  playerPosX)
        #playerPosX = min(screenSizeX-1, playerPosX)
        #playerPosY = max(0,  playerPosY)
        #playerPosY = min(screenSizeY-1, playerPosY)


if __name__ == '__main__':
    screenSetup()
    curses.wrapper(main)