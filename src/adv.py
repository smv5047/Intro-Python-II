from room import Room
from player import Player
from item import Sword, Shield

# Declare all items

master = Sword("Master Sword", "The Triforce is strong in this one", 8)
hylian = Shield("Hylian Shield", "Defend against your enemies", 10)
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [master]),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [hylian]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}

line_break = "///////////////////////////////////////////////"

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
ready = True
player1 = Player("Player 1", room['outside'])


while ready == True:
    # Write a loop that:
    #
    # * Prints the current room name
    print(player1.current_room)
# * Prints the current description (the textwrap module might be useful here).
    print(player1.current_room.description)
    if len(player1.current_room.items) > 0:
        for item in player1.current_room.items:
            print(f'The {item} is laying in the room')
        # print(f'The {player1.current_room.items.name} is laying in the room')
    if len(player1.items) > 0:

        for item in player1.items:
            print(f'Player has the {item.name}')
        # for item in len(player1.current_room.items):
        #     print(player1.current_room.items)
# * Waits for user input and decides what to do.
#
#
# If the user enters "q", quit the game.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed

    print("***Type q to quit***")
    print(line_break)
    print("***Type get item to pick up an item or drop item to drop one***")
    print(line_break)
    choice = input("Please enter a direction: n, e, s, w  ")

    if (choice == 'q'):
        break
    elif (choice == 'n'):
        if player1.current_room.n_to is not None:
            player1.current_room = player1.current_room.n_to
        else:
            print("That's a dead-end, be careful or you might end up dead.")
    elif (choice == 'e'):
        if player1.current_room.e_to is not None:
            player1.current_room = player1.current_room.e_to
    elif (choice == 's'):
        if player1.current_room.s_to is not None:
            player1.current_room = player1.current_room.s_to
    elif (choice == 'w'):
        if player1.current_room.w_to is not None:
            player1.current_room = player1.current_room.w_to
    elif (choice == 'get item'):
        item_choice = input("please enter which item to pickup ")
        for item in player1.current_room.items:
            if (item.name == item_choice):
                player1.get_item(item_choice)
                player1.current_room.items.remove(item)
            else:
                print(f'{item_choice} is not a valid selection')
    elif (choice == 'drop item'):
        drop_choice = input("please enter which item to drop ")
        for item in player1.items:
            if (item.name == drop_choice):
                player1.items.remove(item)
                player1.current_room.items.append(item)
            else:
                print(f'{item_choice} is not held by the player')
    else:
        print("Please enter a valid command: n, e, s, w, or q")
