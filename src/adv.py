from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


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
# * Waits for user input and decides what to do.
#
#
# If the user enters "q", quit the game.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed
    print("***Type q to quit***")
    choice = input("Please enter a direction: n, e, s, w  ")
    print(player1.current_room.n_to)
    try:
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
    except:
        print("Please enter a valid command: n, e, s, w, or q")
