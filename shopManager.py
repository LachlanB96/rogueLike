import curses
from inventoryManager import *

def shopManagerWelcome(inventory, screen):
    screen.clear()
    screenBorders(screen)
    moduleNumber = 1
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    screen.addstr(titlePosY, titlePosX, 'SHOP', curses.color_pair(13))
    screen.addstr(bodyPosY, bodyPosX, ("Hello, would you like to buy or sell?"))
    screen.addstr(bodyPosY + 2, bodyPosX, ("Press 'b' to buy"), curses.color_pair(13))
    screen.addstr(bodyPosY + 3, bodyPosX, ("Press 's' to sell"), curses.color_pair(11))
    screen.addstr(bodyPosY + 4, bodyPosX, ("Press 'q' to leave"), curses.color_pair(5))
    shopManagerGamble(inventory, screen)
    shopManagerBuy(inventory, screen)
    shopManagerSell(inventory, screen)
    inShop = True
    buyingShop = False
    sellingShop = False
    gambleShop = False
    while inShop:
        key = screen.getch()
        if key == ord('q'):
            inShop = False
        elif key == ord('b'):
            buyingShop = True
            inShop = False
        elif key == ord('s'):
            inventory = shopManagerSell(inventory, screen)
            inShop = False


        while buyingShop:
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
                buyingShop = False
    return inventory

def shopManagerGamble(inventory, screen):
    moduleNumber = 2
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    screen.addstr(titlePosY, titlePosX, 'GAMBLING', curses.color_pair(13))

def shopManagerBuy(inventory, screen):
    moduleNumber = 3
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    screen.addstr(titlePosY, titlePosX, 'BUYING', curses.color_pair(13))
    screen.addstr(bodyPosY, bodyPosX, ("Press 'l' to buy a log for 2 gold"), curses.color_pair(7))
    screen.addstr(bodyPosY + 1, bodyPosX, ("Press 'a' to buy an axe for 5 gold"), curses.color_pair(11))
    screen.addstr(bodyPosY + 2, bodyPosX, ("Press 'f' to buy a fishing rod for 3 gold"), curses.color_pair(2))
    screen.addstr(bodyPosY + 4, bodyPosX, ("Press 'q' to leave"), curses.color_pair(13))
    screen.addstr(bodyPosY + 5, bodyPosX, ("Press 's' to sell"), curses.color_pair(11))


def shopManagerSell(inventory, screen):
    moduleNumber = 4
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    screen.addstr(titlePosY, titlePosX, 'SELLING', curses.color_pair(13))
