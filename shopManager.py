import curses
from inventoryManager import *

def shopManagerWelcome(inventory, screen, focus=False):
    moduleNumber = 1
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    if focus:
        screen.addstr(titlePosY, titlePosX, 'SHOP', curses.color_pair(13))
        screen.addstr(bodyPosY, bodyPosX, ("Hello, would you like to buy or sell?"))
        screen.addstr(bodyPosY + 2, bodyPosX, ("Press 'b' to buy"), curses.color_pair(13))
        screen.addstr(bodyPosY + 3, bodyPosX, ("Press 's' to sell"), curses.color_pair(11))
        screen.addstr(bodyPosY + 4, bodyPosX, ("Press 'q' to leave"), curses.color_pair(5))
    else:
        screen.addstr(titlePosY, titlePosX, 'SHOP')
        screen.addstr(bodyPosY, bodyPosX, ("Hello, would you like to buy or sell?"))
        screen.addstr(bodyPosY + 2, bodyPosX, ("Press 'b' to buy"))
        screen.addstr(bodyPosY + 3, bodyPosX, ("Press 's' to sell"))
        screen.addstr(bodyPosY + 4, bodyPosX, ("Press 'q' to leave"))

def shopManagerGamble(inventory, screen, focus=False):
    moduleNumber = 2
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    if focus:
        screen.addstr(titlePosY, titlePosX, 'GAMBLING', curses.color_pair(13))
        screen.addstr(bodyPosY + 2, bodyPosX, ("Press '1' to gamble   1 coins"), curses.color_pair(15))
        screen.addstr(bodyPosY + 3, bodyPosX, ("Press '2' to gamble   5 coins"), curses.color_pair(15))
        screen.addstr(bodyPosY + 4, bodyPosX, ("Press '3' to gamble  20 coins"), curses.color_pair(15))
        screen.addstr(bodyPosY + 5, bodyPosX, ("Press '4' to gamble  50 coins"), curses.color_pair(15))
        screen.addstr(bodyPosY + 6, bodyPosX, ("Press '5' to gamble 100 coins"), curses.color_pair(15))
        screen.addstr(bodyPosY + 7, bodyPosX, ("Press '6' to gamble 500 coins"), curses.color_pair(15))
    else:
        screen.addstr(titlePosY, titlePosX, 'GAMBLING')
        screen.addstr(bodyPosY + 2, bodyPosX, ("Press '1' to gamble   1 coins"))
        screen.addstr(bodyPosY + 3, bodyPosX, ("Press '2' to gamble   5 coins"))
        screen.addstr(bodyPosY + 4, bodyPosX, ("Press '3' to gamble  20 coins"))
        screen.addstr(bodyPosY + 5, bodyPosX, ("Press '4' to gamble  50 coins"))
        screen.addstr(bodyPosY + 6, bodyPosX, ("Press '5' to gamble 100 coins"))
        screen.addstr(bodyPosY + 7, bodyPosX, ("Press '6' to gamble 500 coins"))

def shopManagerBuy(inventory, screen, focus=False):
    moduleNumber = 3
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    if focus:
        screen.addstr(titlePosY, titlePosX, 'BUYING', curses.color_pair(13))
        screen.addstr(bodyPosY, bodyPosX, ("Press 'l' to buy a log for 2 gold"), curses.color_pair(7))
        screen.addstr(bodyPosY + 1, bodyPosX, ("Press 'a' to buy an axe for 5 gold"), curses.color_pair(11))
        screen.addstr(bodyPosY + 2, bodyPosX, ("Press 'f' to buy a fishing rod for 3 gold"), curses.color_pair(2))
        screen.addstr(bodyPosY + 4, bodyPosX, ("Press 'q' to leave"), curses.color_pair(13))
        screen.addstr(bodyPosY + 5, bodyPosX, ("Press 's' to sell"), curses.color_pair(11))
    else:
        screen.addstr(titlePosY, titlePosX, 'BUYING')
        screen.addstr(bodyPosY, bodyPosX, ("Press 'l' to buy a log for 2 gold"))
        screen.addstr(bodyPosY + 1, bodyPosX, ("Press 'a' to buy an axe for 5 gold"))
        screen.addstr(bodyPosY + 2, bodyPosX, ("Press 'f' to buy a fishing rod for 3 gold"))
        screen.addstr(bodyPosY + 4, bodyPosX, ("Press 'q' to leave"))
        screen.addstr(bodyPosY + 5, bodyPosX, ("Press 's' to sell"))


def shopManagerSell(inventory, screen, focus=False):
    moduleNumber = 4
    titlePosY, titlePosX = screenPositioner(moduleNumber, "title")
    bodyPosY, bodyPosX = screenPositioner(moduleNumber, "body")
    if focus:
        screen.addstr(titlePosY, titlePosX, 'SELLING', curses.color_pair(13))
        i = 0 #counter for list items
        for item in set(inventory):
            screen.addstr(bodyPosY + i, bodyPosX, (str(inventory.count(item)) + " x " + item))
            i += 1
    else:
        screen.addstr(titlePosY, titlePosX, 'SELLING')
        i = 0 #counter for list items
        for item in set(inventory):
            screen.addstr(bodyPosY + i, bodyPosX, (str(inventory.count(item)) + " x " + item))
            i += 1

def shopManagerManager(inventory, screen):
    gamblingShop = False
    sellShop = False
    buyingShop = False
    inShop = True
    while inShop:
        screen.clear()
        screenBorders(screen)
        screen.addstr(10, 20, ("A"))
        shopManagerWelcome(inventory, screen, True)
        shopManagerGamble(inventory, screen)
        shopManagerBuy(inventory, screen)
        shopManagerSell(inventory, screen)
        screen.addstr(10, 20, ("G"))
        key = screen.getch()
        screen.addstr(10, 20, ("H"))
        if key == ord('q'):
            inShop = False
        elif key == ord('b'):
            screen.addstr(10, 20, ("E"))
            inShop = False
            buyingShop = True
        elif key == ord('s'):
            sellShop = True
            inShop = False
        screen.addstr(10, 20, ("D"))


        while buyingShop:
            screen.clear()
            screenBorders(screen)
            screen.addstr(10, 20, ("A"))
            shopManagerWelcome(inventory, screen)
            shopManagerGamble(inventory, screen)
            shopManagerBuy(inventory, screen, True)
            shopManagerSell(inventory, screen)
            screen.addstr(10, 20, ("B"))
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
                buyingShop = False
    screen.addstr(10, 20, ("C"))
    return inventory
