stuff = {'green wood': 350, 'stone block': 146, 'large salmon': 14,
         'great axe': 2, 'iron pickaxe': 1, 'starmetal ice gauntlet': 1}

dragon_loot = ['dragon skull', 'obsidian pickaxe', 'starmetal ice gauntlet', 'ruby ring']


def display_inventory(inventory):
    """this a doc string"""
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inv, dragon_loot):
    copy_stuff = inv.copy()
    for item in dragon_loot:
        if item in copy_stuff:
            copy_stuff[item] += 1
        else:
            copy_stuff[item] = 1
    return copy_stuff


print(stuff)
stuff = add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)