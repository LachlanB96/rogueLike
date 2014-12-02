import curses
import os

def screenSetup():
    termSizeX = "60"
    termSizeY = "100"
    curses.use_env(True)
    os.environ['LINES'] = termSizeX
    os.environ['COLS'] = termSizeY


def screenBorders(screen):
    termSizeX = int(os.environ['LINES'])
    termSizeY = int(os.environ['COLS'])
    for i in range(0, termSizeX):
        screen.addstr(i, 0, '|')
        screen.addstr(i, int(termSizeY/2), '|')
        screen.addstr(i, (termSizeY - 2), '|')
    for i in range(0, termSizeY - 1):
        screen.addstr(0, i, '-')
        screen.addstr(2, i, '-')
        screen.addstr(int(termSizeX/2), i, '-')
        screen.addstr(int(termSizeX/2) + 2, i, '-')
        screen.addstr(termSizeX - 1, i, '-')

def screenPositioner(moduleNumber, component):
    if moduleNumber == 1:
        if component == "title":
            return 1, 3
        elif component == "body":
            return 3, 1
        elif component == "bodyCentre":
            return 3
    elif moduleNumber == 2:
        if component == "title":
            return 1, int(int(os.environ['COLS'])/2) + 3
        elif component == "body":
            return 3, int(int(os.environ['COLS'])/2) + 1
        elif component == "bottom":
            return int(int(os.environ['LINES'])/2-1), int(int(os.environ['COLS'])/2) + 1
    elif moduleNumber == 3:
        if component == "title":
            return int(int(os.environ['LINES'])/2+1), 3
        elif component == "body":
            return int(int(os.environ['LINES'])/2+3), 1
    elif moduleNumber == 4:
        if component == "title":
            return int(int(os.environ['LINES'])/2+1), int(int(os.environ['COLS'])/2) + 3
        elif component == "body":
            return int(int(os.environ['LINES'])/2+3), int(int(os.environ['COLS'])/2) + 1
    elif moduleNumber == 6: #weather
        if component == "body":
            return int(os.environ['LINES']) - 1, 1

def moduleSize():
    return int(int(os.environ['COLS'])/2)-1, int(int(os.environ['LINES'])/2)-3

def moduleReposition(key, modulePositions, screen):
    if key == ord('1'):
        module = 1
    elif key == ord('2'):
        module = 2
    elif key == ord('3'):
        module = 3
    elif key == ord('4'):
        module = 4
    chosingOption = True
    while chosingOption:
        option = screen.getch()
        if option == ord('m'):
            #http://stackoverflow.com/a/13149770
            modulePositions[list(modulePositions.keys())[list(modulePositions.values()).index(module)]] = modulePositions['map']
            modulePositions['map'] = module
            chosingOption = False
        elif option == ord('a'):
            modulePositions[list(modulePositions.keys())[list(modulePositions.values()).index(module)]] = modulePositions['actions']
            modulePositions['actions'] = module
            chosingOption = False
        elif option == ord('i'):
            modulePositions[list(modulePositions.keys())[list(modulePositions.values()).index(module)]] = modulePositions['inventory']
            modulePositions['inventory'] = module
            chosingOption = False
        elif option == ord('s'):
            modulePositions[list(modulePositions.keys())[list(modulePositions.values()).index(module)]] = modulePositions['skills']
            modulePositions['skills'] = module
            chosingOption = False
        elif option == ord('q'):
            modulePositions[list(modulePositions.keys())[list(modulePositions.values()).index(module)]] = modulePositions['quests']
            modulePositions['quests'] = module
            chosingOption = False

    return modulePositions
