#Importing libraries
import time
import json
import player_class


#Opening json files for later use
with open("./json_files/item_data.json", "r") as read_file:
    itemdata = json.load(read_file)

with open("./json_files/room_data.json", "r") as read_file:
    roomdata = json.load(read_file)

#Attaching player class to object
plr = player_class.player()


#ITEM FUNCTIONS
#Adding item to inventory
def item_add(item):
    plr.inventory.append(item)
    
#Removing item from inventory

#Displaying items in player inventory

#FIGHTING FUNCTIONS
#

#ROOM FUNCTIONS
#

#INVESTIGATION FUNCTIONS
#

#SCORING FUNCTIONS
#

