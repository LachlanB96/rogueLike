import curses
from screenManager import *

def helpManagerDisplay(screen, moduleNumber):
    if not moduleNumber > 7:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'HELP', curses.color_pair(13))
        screen.addstr(bodyPosY + 0, bodyPosX, "Created by Lachlan Brown, BlueMint Games", curses.color_pair(3))
        screen.addstr(bodyPosY + 1, bodyPosX, "  - RogueLike, 2015, V0.1.2a", curses.color_pair(3))
        screen.addstr(bodyPosY + 2, bodyPosX, "Find BlueMint on GitHub", curses.color_pair(3))
        screen.addstr(bodyPosY + 4, bodyPosX, "Press WASD to move", curses.color_pair(15))
        screen.addstr(bodyPosY + 5, bodyPosX, "Explore the Map, and read the action", curses.color_pair(15))
        screen.addstr(bodyPosY + 6, bodyPosX, "screen for prompts. There is no goal.", curses.color_pair(15))
        screen.addstr(bodyPosY + 8, bodyPosX, "To change screens, press 1-4 (depending on", curses.color_pair(5))
        screen.addstr(bodyPosY + 9, bodyPosX, "screen), then: m=map,a=actions,i=inventory", curses.color_pair(5))
        screen.addstr(bodyPosY + 10, bodyPosX, "s=skills,q=quests,t=stats,h=help", curses.color_pair(5))