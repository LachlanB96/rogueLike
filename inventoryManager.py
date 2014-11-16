import curses
from screenManager import *

def inventoryManager(inventory, screen, inventoryPosY, moduleNumber):
    if not moduleNumber == 5:
        titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
        bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
        screen.addstr(titlePosY, titlePosX, 'INVENTORY', curses.color_pair(13))
        i = 0 #counter for list items
        for item in set(inventory):
            screen.addstr(bodyPosY + i, bodyPosX, (str(inventory.count(item)) + " x " + item))
            i += 1

def itemPresentInInventory(item, inventory):
    if item in inventory:
        return True

def removeItemFromInventory(item, inventory, amount):
    for i in range(0,amount):
        inventory.remove(item)
    return inventory