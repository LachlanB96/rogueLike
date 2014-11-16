import curses
import random
from screenManager import *


def questManagerDisplay(screen, activeQuests, moduleNumber):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'QUESTS', curses.color_pair(13))
        screen.addstr(bodyPosY, bodyPosX, ("Town Coord | Quest Coord | Type | Reward"))
        i = 1 #counter for list items
        for quest in activeQuests:
        
            screen.addstr(bodyPosY + i, bodyPosX, ("  " + quest[0] + "  |   " + quest[1] + "   | " + quest[2] + " | " + quest[4] + " " + quest[3]))
            i += 1

def questManagerNew(currentMap, activeQuests, playerPosX, playerPosY):
    questPosX = random.randint(-10,10) + playerPosX
    questPosY = random.randint(-10,10) + playerPosY
    while not currentMap[questPosX][questPosY] == "grass":
        questPosX = random.randint(-10,10) + playerPosX
        questPosY = random.randint(-10,10) + playerPosY
    currentMap[questPosX][questPosY] = "quest"
    activeQuests.append((str(str(playerPosX) + "," + str(playerPosY)),(str(questPosX) + "," + str(questPosY)),"kill","money","200"))
    return currentMap, activeQuests