import curses
import os

def screenSetup():
    termSizeY = "70"
    termSizeX = "240"
    curses.use_env(True)
    os.environ['LINES'] = termSizeY
    os.environ['COLS'] = termSizeX


def screenBorders(screen):
    termSizeY = int(os.environ['LINES'])
    termSizeX = int(os.environ['COLS'])
    for i in range(0, termSizeY):
        screen.addstr(i, 0, '|')
        screen.addstr(i, int(termSizeX/4), '|')
        screen.addstr(i, int(termSizeX/2), '|')
        screen.addstr(i, (int(termSizeX/2) + int(termSizeX/4)), '|')
        screen.addstr(i, (termSizeX - 2), '|')
    for i in range(0, termSizeX - 1):
        screen.addstr(0, i, '-')
        screen.addstr(2, i, '-')
        screen.addstr(int(termSizeY/2), i, '-')
        screen.addstr(int(termSizeY/2) + 2, i, '-')
        screen.addstr(termSizeY - 1, i, '-')

def screenPositioner(moduleNumber, component):
    if moduleNumber == 0:
        if component == "title":
            return 1, 3
        elif component == "body":
            return 3, 1
        elif component == "bodyCentre":
            return 3
    elif moduleNumber == 1:
        if component == "title":
            return 1, int(int(os.environ['COLS'])/4) + 3
        elif component == "body":
            return 3, int(int(os.environ['COLS'])/4) + 1
        elif component == "bottom":
            return int(int(os.environ['LINES'])/2-1), int(int(os.environ['COLS'])/4) + 1
    elif moduleNumber == 2:
        if component == "title":
            return 1, int(int(os.environ['COLS'])/2) + 3
        elif component == "body":
            return 3, int(int(os.environ['COLS'])/2) + 1
        elif component == "bottom":
            return int(int(os.environ['LINES'])/2-1), int(int(os.environ['COLS'])/2) + 1
    elif moduleNumber == 3:
        if component == "title":
            return 1, int(int(os.environ['COLS'])/2 + int(int(os.environ['COLS'])/4)) + 3
        elif component == "body":
            return 3, int(int(os.environ['COLS'])/2 + int(int(os.environ['COLS'])/4)) + 1
        elif component == "bottom":
            return int(int(os.environ['LINES'])/2-1), int(int(os.environ['COLS'])/2 + int(int(os.environ['COLS'])/4)) + 1
    elif moduleNumber == 4:
        if component == "title":
            return int(int(os.environ['LINES'])/2+1), 3
        elif component == "body":
            return int(int(os.environ['LINES'])/2+3), 1
    elif moduleNumber == 5:
        if component == "title":
            return int(int(os.environ['LINES'])/2+1), int(int(os.environ['COLS'])/4) + 3
        elif component == "body":
            return int(int(os.environ['LINES'])/2+3), int(int(os.environ['COLS'])/4) + 1
    elif moduleNumber == 6:
        if component == "title":
            return int(int(os.environ['LINES'])/2+1), int(int(os.environ['COLS'])/2) + 3
        elif component == "body":
            return int(int(os.environ['LINES'])/2+3), int(int(os.environ['COLS'])/2) + 1
    elif moduleNumber == 99: #weather
        if component == "body":
            return int(os.environ['LINES']) - 1, 1

def moduleSize():
    return int(int(os.environ['COLS'])/4)-1, int(int(os.environ['LINES'])/2)-3

def moduleReposition(module, modulePositions, screen):
    chosingOption = True
    moduleKeys = {'m':'map','a':'actions','i':'inventory','s':'skills','q':'quests','t':'stats','h':'help','d':'debug'}
    while chosingOption:
        option = screen.getch()
        if not option == -1:
            option = chr(option)
            modulePositions.remove(moduleKeys[option])
            modulePositions.insert((int(module) - 1), moduleKeys[option])
            chosingOption = False
    return modulePositions
