import curses

def skillManagerDisplay(screen, skillManagerDisplayX, skillManagerDisplayY, skills):
    screen.addstr(skillManagerDisplayY, skillManagerDisplayX, 'SKILLS', curses.color_pair(10))
    screen.addstr(skillManagerDisplayY + 1, skillManagerDisplayX, ("attack | " + skillManagerExperienceBar(skills['attack'])), curses.color_pair(13))

#class Skill(name, colour)


def skillManagerExperienceBar(skill):
    level = 1
    while skill - 10*2**(level - 1) > 0:
        skill -= 10*2**(level - 1)
        level +=1
    level -= 1
    expUntilNextLevel = -1*(skill - 10*2**(level))
    percentGotUntilNextLevel = 100*skill/(expUntilNextLevel+skill)
    percentageBar = ""
    for i in range(0,25):
        if percentGotUntilNextLevel > 0:
            percentageBar += "+"
            percentGotUntilNextLevel -= 4
        else:
            percentageBar += "-"
    return (str(level) + " |" + str(percentageBar) + "|")


    #10:1,30:2,70:3,150:4