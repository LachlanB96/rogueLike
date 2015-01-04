import curses
from screenManager import *

def statManagerDisplay(screen, moduleNumber, playerStats):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'STATS', curses.color_pair(13))
        screen.addstr(bodyPosY + 1, bodyPosX, "Health: " + str(playerStats[0]), curses.color_pair(5))
        screen.addstr(bodyPosY + 2, bodyPosX, "Mana: " + str(playerStats[1]), curses.color_pair(2))
        screen.addstr(bodyPosY + 3, bodyPosX, "Attack: " + str(playerStats[2]), curses.color_pair(6))
        screen.addstr(bodyPosY + 4, bodyPosX, "Defense: " + str(playerStats[3]), "name"), curses.color_pair(6))
        screen.addstr(bodyPosY + 5, bodyPosX, "Speed: " + str(playerStats[4]), "name"), curses.color_pair(6))
        screen.addstr(bodyPosY + 6, bodyPosX, "Left Wield: " + itemIDLookup(playerStats[5], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 7, bodyPosX, "Right Wield: " + itemIDLookup(playerStats[6], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 8, bodyPosX, "Head: " + itemIDLookup(playerStats[7], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 9, bodyPosX, "Neck: " + itemIDLookup(playerStats[8], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 10, bodyPosX, "Torso: " + itemIDLookup(playerStats[9], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 11, bodyPosX, "Left Arm: " + itemIDLookup(playerStats[10], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 12, bodyPosX, "Right Arm: " + itemIDLookup(playerStats[11], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 13, bodyPosX, "Legs: " + itemIDLookup(playerStats[12], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 14, bodyPosX, "Feet: " + itemIDLookup(playerStats[13], "name"), curses.color_pair(13))
        screen.addstr(bodyPosY + 15, bodyPosX, "Pet/Slave: " + itemIDLookup(playerStats[14], "name"), curses.color_pair(13))

def itemIDLookup(itemID, lookupType):
    