import curses
from screenManager import *

def debugManagerDisplay(screen, moduleNumber, debugLog):
    if not moduleNumber > 7:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'DEBUG', curses.color_pair(13))
        for line in debugLog:
            screen.addstr(bodyPosY + i, bodyPosX, (line))
            i += 1