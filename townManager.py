import curses
from screenManager import *

def townManagerDisplay(screen, moduleNumber):
    if not moduleNumber> 7:
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

def townGenerate(matrix, posX, posY, size, townsList):
    topLeftX = posX - size - 1
    topLeftY = posY - 2
    town = Town((topLeftX, topLeftY), (topLeftX + size*2, topLeftY + size*2), matrix)
    matrix = town.generate(matrix)
    townsList.append(town)
    return matrix, townsList

class Town():
    def __init__(self, topLeft, bottomRight, matrix):
        self.topLeftX, self.topLeftY = topLeft
        self.bottomRightX, self.bottomRightY = bottomRight
        self.size = self.topLeftX - self.bottomRightX
        self.width = self.size * 2 + 2

    def generate(self, matrix):
        for i in range(self.width):
            for j in range(self.width):
                matrix[self.topLeftX+i][self.topLeftY+j] = "grass"
        for i in range(-self.size,self.size):
            matrix[self.topLeftX+i][self.topLeftY - 1] = "townWall"
            matrix[self.topLeftX+i][self.topLeftY + self.size*2] = "townWall"
            matrix[self.topLeftX-self.size][self.topLeftY+i+self.size] = "townWall"
            matrix[self.topLeftX+self.size][self.topLeftY+i+self.size] = "townWall"
        matrix[self.topLeftX+self.size][self.topLeftY-1] = "townWall"
        matrix[self.topLeftX+self.size][self.topLeftY+self.size*2] = "townWall"
        matrix[self.topLeftX-1][self.topLeftY+self.size*2] = "alter"
        matrix[self.topLeftX][self.topLeftY+self.size*2] = "alter"
        matrix[self.topLeftX+1][self.topLeftY+self.size*2] = "alter"
        matrix[self.topLeftX-1][self.topLeftY+self.size*2+1] = "alter"
        matrix[self.topLeftX][self.topLeftY+self.size*2+1] = "alter"
        matrix[self.topLeftX+1][self.topLeftY+self.size*2+1] = "alter"
        return matrix