import curses
from inventoryManager import *

def shopManagerWelcome(inventory, screen, descriptionBoxX, inventoryPosY):
    screen.addstr(3, descriptionBoxX, ("Hello, would you like to buy or sell?"))
    screen.addstr(4, descriptionBoxX, ("Press 'b' to buy"), curses.color_pair(13))
    screen.addstr(5, descriptionBoxX, ("Press 's' to sell"), curses.color_pair(11))
    screen.addstr(6, descriptionBoxX, ("Press 'q' to leave"), curses.color_pair(5))
    inShop = True
    while inShop:
        key = screen.getch()
        if key == ord('q'):
            inShop = False
        elif key == ord('b'):
            inventory = shopManagerBuy(inventory, screen, descriptionBoxX, inventoryPosY)
            inShop = False
        elif key == ord('s'):
            inventory = shopManagerSell(inventory, screen, descriptionBoxX)
            inShop = False
    return inventory


def shopManagerBuy(inventory, screen, descriptionBoxX, inventoryPosY):
    print ("W")
    screen.addstr(4, descriptionBoxX, ("Press 'l' to buy a log for 2 gold"), curses.color_pair(7))
    screen.addstr(5, descriptionBoxX, ("Press 'a' to buy an axe for 5 gold"), curses.color_pair(11))
    screen.addstr(6, descriptionBoxX, ("Press 'f' to buy a fishing rod for 3 gold"), curses.color_pair(2))
    screen.addstr(7, descriptionBoxX, ("Press 'q' to leave"), curses.color_pair(13))
    screen.addstr(8, descriptionBoxX, ("Press 's' to sell"), curses.color_pair(11))
    inShop = True
    while inShop:
        inventoryManager(inventory, screen, inventoryPosY)
        key = screen.getch()
        if key == ord('l'):
            if inventory.count("gold") >= 2:
                inventory.append("logs")
                inventory = removeItemFromInventory("gold", inventory, 2)
        elif key == ord('f'):
            if inventory.count("gold") >= 3:
                inventory.append("fishingRod")
                inventory = removeItemFromInventory("gold", inventory, 3)
        elif key == ord('a'):
            if inventory.count("gold") >= 5:
                inventory.append("axe")
                inventory = removeItemFromInventory("gold", inventory, 5)
        elif key == ord('q'):
            inShop = False
        elif key == ord('s'):
            inventory = shopManagerSell(inventory, screen, descriptionBoxX)
            inShop = False
    return inventory

def shopManagerSell(inventory, screen, descriptionBoxX):

    print("dfg")