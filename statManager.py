import curses
from screenManager import *

def statManagerDisplay(screen, skills, moduleNumber):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'STATS', curses.color_pair(13))
        screen.addstr(bodyPosY + 1, bodyPosX, "Health: 100", curses.color_pair(5))
        screen.addstr(bodyPosY + 2, bodyPosX, "Mana: 100", curses.color_pair(2))
        screen.addstr(bodyPosY + 3, bodyPosX, "Attack: 100", curses.color_pair(6))
        screen.addstr(bodyPosY + 4, bodyPosX, "Defense: 100", curses.color_pair(6))
        screen.addstr(bodyPosY + 5, bodyPosX, "Speed: 100", curses.color_pair(6))
        screen.addstr(bodyPosY + 6, bodyPosX, "Left Wield: Fist", curses.color_pair(13))
        screen.addstr(bodyPosY + 7, bodyPosX, "Right Wield: Fist", curses.color_pair(13))
        screen.addstr(bodyPosY + 8, bodyPosX, "Head: Bronze Helmet", curses.color_pair(13))
        screen.addstr(bodyPosY + 9, bodyPosX, "Neck: Sapphire Amulet", curses.color_pair(13))
        screen.addstr(bodyPosY + 10, bodyPosX, "Torso: Broken Bronze Body Plate", curses.color_pair(13))
        screen.addstr(bodyPosY + 11, bodyPosX, "Left Arm: Enchanted Amulet", curses.color_pair(13))
        screen.addstr(bodyPosY + 12, bodyPosX, "Right Arm: Hidden Knife", curses.color_pair(13))
        screen.addstr(bodyPosY + 13, bodyPosX, "Legs: Bronze Leggings", curses.color_pair(13))
        screen.addstr(bodyPosY + 14, bodyPosX, "Feet: Iron Boots", curses.color_pair(13))
        screen.addstr(bodyPosY + 15, bodyPosX, "Pet/Slave: Pikachu", curses.color_pair(13))
