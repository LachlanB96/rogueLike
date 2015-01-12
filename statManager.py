import curses
from screenManager import *
import xlrd

def statManagerDisplay(screen, moduleNumber, playerStats, armourUpdated):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'STATS', curses.color_pair(13))
        screen.addstr(bodyPosY + 1, bodyPosX, "Health: " + str(playerStats[0]), curses.color_pair(5))
        screen.addstr(bodyPosY + 2, bodyPosX, "Mana: " + str(playerStats[1]), curses.color_pair(2))
        screen.addstr(bodyPosY + 3, bodyPosX, "Attack: " + str(playerStats[2]), curses.color_pair(6))
        screen.addstr(bodyPosY + 4, bodyPosX, "Defense: " + str(playerStats[3]), curses.color_pair(6))
        screen.addstr(bodyPosY + 5, bodyPosX, "Speed: " + str(playerStats[4]), curses.color_pair(6))
        if armourUpdated:
            statManagerDisplayArmour(screen, titlePosY, titlePosX, bodyPosY, bodyPosX, playerStats)

def statManagerDisplayArmour(screen, titlePosY, titlePosX, bodyPosY, bodyPosX, playerStats):
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
    workbook = xlrd.open_workbook('itemDescriptions.xlsx')
    worksheet = workbook.sheet_by_name('Stats')
    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1
    curr_row = 1
    while curr_row < num_rows:
        if worksheet.cell_value(curr_row, 0) == itemID:
            if lookupType == 'name':
                return str(worksheet.cell_value(curr_row, 1) + " " + worksheet.cell_value(curr_row, 2))
            elif lookupType == "stats":
                return str("A: ", worksheet.cell_value(curr_row, 4), ". D: ", worksheet.cell_value(curr_row, 5), ". S: ", worksheet.cell_value(curr_row, 6))
            elif lookupType == "rarity":
                return str("Rareness: ", worksheet.cell_value(curr_row, 3))
            else:
                return str("NULL")
        curr_row += 1