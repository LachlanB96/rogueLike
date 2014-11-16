import curses
from screenManager import *

def skillManagerDisplay(screen, skills, moduleNumber):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'SKILLS', curses.color_pair(13))
        skillCounter = 0
        for skill in skills:
            screen.addstr(bodyPosY + skillCounter, bodyPosX, (skill + " | " + skillManagerExperienceBar(skills[skill])), curses.color_pair(13))
            skillCounter += 1

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

def skillManagerExperience(skills, skill, experienceEarned):
    if not skill in skills:
        skills[skill] = experienceEarned
    else:
        skills[skill] += experienceEarned
    return skills


    #10:1,30:2,70:3,150:4