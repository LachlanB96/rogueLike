import curses

def inventoryManager(inventory, screen, inventoryPosY):
    screen.addstr(inventoryPosY, 0, 'INVENTORY', curses.color_pair(13))
    i = 2 #counter for list items
    for item in inventory:
        screen.addstr(inventoryPosY + i, 0, item)
        i += 1

def itemPresentInInventory(item, inventory):
    if item in inventory:
        return True

def removeItemFromInventory(item, inventory):
    inventory.remove(item)
    return inventory