from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



def movement():

current_room = "outside"

    while current_room != 'q':
        print(f'You are in {current_room}.')
        
        available_direction = 'none'

        if current_room == 'outside':
            available_direction = 'n'
        elif current_room == 'foyer':
            available_direction ='n, s, e'
        elif current_room == 'overlook':
            available_direction = 's'
        elif current_room == 'narrow':
            available_direction = 'w, n'
        elif current_room == 'treasure':
            available_direction = 's'

        decision = input(f'You can go {available_direction}, enter your choice')

        try:
            decision = str(decision)
        except ValueError:
            print('Please enter a correct response')
            continue

        if current_room == 'outside' and decision == 'n':
            current_room = 'foyer'
        elif current_room == 'foyer' and decision == 's':
            current_room = 'outside'
        elif current_room == 'foyer' and decision == 'n':
            current_room = 'overlook'
        elif current_room == 'foyer' and decision == 'e':
            current_room = 'outside'    
        elif current_room == 'overlook' and decision == 's':
            current_room = 'foyer'
        elif current_room == 'narrow' and decision == 'w':
            current_room = 'foyer'
        elif current_room == 'narrow' and decision == 'n':
            current_room = 'treasure'
        elif current_room == 'treasure' and decision == 's':
            current_room = 'narrow'

        print(f'Moving into the {current_room}')
