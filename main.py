import curses
import random

def mapGenerate(mapSizeX, mapSizeY, trees=5, towns=1, shops=2, monsters=4):
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
    for i in range(mapSizeY):
        for j in range (mapSizeX):
            tileSeed = random.randint(0, 100)
            if tileSeed in treeRange: tileType = "tree"
            elif tileSeed in townsRange: tileType = "town"
            elif tileSeed in shopsRange: tileType = "shop"
            elif tileSeed in monstersRange: tileType = "monster"
            else: tileType = "grass"
            matrix[j][i] = tileType
    return matrix


def main(screen):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.curs_set(0)
    screen.nodelay(True)
    screen.clear()
    my, mx = screen.getmaxyx()
    mapSizeX = int(mx/2)
    mapSizeY = my - int(my/2)
    descriptionBoxX = mapSizeX + int(mapSizeX/10)
    x = int(mapSizeX/2)
    y = int(mapSizeY/2)
    ax = 0
    ay = 0
    currentMap = mapGenerate(mapSizeX, mapSizeY)

    while True:
        screen.clear()
        for i in range(mapSizeY - 1):
            for j in range (mapSizeX - 1):
                if currentMap[j][i] == "tree": screen.addstr(i, j, 't', curses.color_pair(3))
                elif currentMap[j][i] == "town": screen.addstr(i, j, 'T', curses.color_pair(14))
                elif currentMap[j][i] == "shop": screen.addstr(i, j, '$', curses.color_pair(15))
                elif currentMap[j][i] == "monster": screen.addstr(i, j, 'M', curses.color_pair(13))
                else: screen.addstr(i, j, ',')
        description = currentMap[x][y]
        screen.addch(y, x, '@', curses.color_pair(12))
        screen.addstr(0, descriptionBoxX, ("(" + str(mx) + ", " + str(my) + ")" + "  " + "(" + str(x) + ", " + str(y) + ")"))
        screen.addstr(1, descriptionBoxX, (description))
        key = screen.getch()

        if key == curses.ERR:
            continue

        if key in [ord('q'), ord('Q')]:
            break
        if key == curses.KEY_LEFT:
            x = x - 1
        elif key == curses.KEY_RIGHT:
            x = x + 1
        elif key == curses.KEY_UP:
            y = y - 1
        elif key == curses.KEY_DOWN:
            y = y + 1

        x = max(0,  x)
        x = min(mx-1, x)
        y = max(0,  y)
        y = min(my-1, y)


if __name__ == '__main__':
    curses.wrapper(main)