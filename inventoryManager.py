import curses
from screenManager import *

def inventoryManager(inventory, screen, inventoryPosY):
    titlePosY, titlePosX = screenPositioner(3, "title")
    screen.addstr(titlePosY, titlePosX, 'INVENTORY', curses.color_pair(13))
    i = 2 #counter for list items
    for item in set(inventory):
        screen.addstr(inventoryPosY + i, 0, (str(inventory.count(item)) + " x " + item))
        i += 1

def itemPresentInInventory(item, inventory):
    if item in inventory:
        return True

def removeItemFromInventory(item, inventory, amount):
    for i in range(0,amount):
        inventory.remove(item)
    return inventory