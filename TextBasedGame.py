# Paul Kenaga
# Develop and submit the “TextBasedGame.py” file using PyCharm.
# Include your full name in a comment at the top of the code.
# Be sure to submit the code that you have completed, even if you did not finish the full game.

# Line separator
def line():
    print('-' * 75)


# Display instructions along with commands
def instructions():
    line()
    print('Welcome to the Alice in Wonderland Text Game!')
    line()
    print(
        '\"You\'re late! You\'re late for a very important date!\n'
        'No time to say hello, good-bye and here is the reason why...\n\n'
        'It is Frabjous day and you, Alice, must save Wonderland!\n\n'
        'Move through this magical realm and collect 6 special items '
        'in your\ninventory to defeat the Red Queen\'s ferocious Jabberwocky.\"'
        '\n\nMove commands: go North, go South, go East, go West\n'
        'Collect command: get \'item name\''
        '\n\n(To exit or restart the game at any point, type \'exit\'.)'
    )
    line()


# Allow player to exit or restart game
def exit_game():
    while True:
        print('Are you sure you want to leave?')
        exit_command = input('Type \'Y\' to EXIT or \'N\' to RESTART: ').lower()
        if exit_command == 'n':
            main()
        if exit_command == 'y':
            line()
            print('\nTake care Alice! See you next time!')
            exit()
        else:
            line()
            print('Invalid response. Try again.')
            line()
            continue


# Allow player to play again or exit if they win
def play_again():
    line()
    while True:
        print('Would you like to play again?')
        start_over = input('Type \'Y\' to RESTART or \'N\' to EXIT: ').lower()
        if start_over == 'y':
            main()
        if start_over == 'n':
            line()
            print('\nSo long Alice! See you next time!')
            exit()
        else:
            line()
            print('Invalid response. Try again.')
            line()
            continue


# Main game function:
def main():
    # Dictionary of rooms, items, and descriptions of items/rooms
    rooms = {
        'Long Hall': {
            'North': 'The Garden',
            'South': 'Dry Landing',
            'East': 'White Rabbit\'s House',
            'West': 'The Mad Hatter\'s House',
            'item': '',
            'desc': 'The room of doors and entrance to Underland.'
        },
        'The Mad Hatter\'s House': {
            'East': 'Long Hall',
            'item': 'Hat',
            'desc': 'The Hatter\'s Hat to be exact! '
                    'Hatter is nothing without his hat and he has\n'
                    'lost his muchness since the queen took him prisoner.\n'
                    'Take it with you to give back to Hatter after taking down the Jabberwocky.'
        },
        'The Garden': {
            'South': 'Long Hall',
            'East': 'Crimms',
            'item': 'Mushroom',
            'desc': 'Taking a bite of one side will make you '
                    'grow taller.\nTaking a bite of the other will make you grow smaller.\n'
                    'A useful tool in an uncommon land.'

        },
        'Crimms': {
            'West': 'The Garden',
            'item': 'Sword',
            'desc': 'The Vorpal Sword is a magical weapon that cannot be damaged.\n'
                    'It is the only weapon powerful enough to take down the Jabberwocky.'

        },
        'Marmoreal': {
            'South': 'White Rabbit\'s House',
            'item': 'Oraculum',
            'desc': 'It tells of each and every day since the beginning.\n'
                    'It will lead you to a victorious Frabjous Day!'
        },
        'White Rabbit\'s House': {
            'North': 'Marmoreal',
            'West': 'Long Hall',
            'item': 'Key',
            'desc': 'Hurry, this Golden Key unlocks '
                    'the door to the beautiful beds of flowers\nand cool fountains in The Garden.'
        },
        'Dry Landing': {
            'North': 'Long Hall',
            'East': 'Tugley Wood',
            'item': 'Shell',
            'desc': 'A gift from the Mock Turtle. It will aide your battle!'
        },
        'Tugley Wood': {
            'West': 'Dry Landing',
            'item': 'Jabberwocky',
            'desc': '\nWith all items collected, the Red Queen\'s Jabberwocky stood no chance!\n'
                    'You returned Mad Hatter\'s Hat and he greeted you with a dance.\n\n'
                    'The Vorpal Sword swung heavy, and silently too,\n'
                    'It took but a minute before cutting right through.\n\n'
                    'And just like that Wonderland was saved. Callooh! Callay!\n'
                    'Everyone now wonders if you\'ll remember Frabjous Day.',
            'desc2': '\nWithout all items, the Jabberwocky laughs.\n'
                     'It used it\'s claws to tear poor Alice to havles.'
        },
    }

    # Check if player has all items in their inventory
    # If all items collected, player wins - can replay or exit
    # Otherwise, player loses - game exits
    def validate_inventory():
        if len(inventory) == len(valid_items):
            print(rooms[current_room]['desc'])
            print('\n\nYou Won Alice!\n')
            play_again()
        else:
            print(rooms[current_room]['desc2'])
            print('\n\nYou Lost Alice :(\n')
            print('Thanks for playing!')
            line()
            exit()

    # Function to display location and inventory
    def display_location():
        print('You are in {}.'.format(current_room))
        while True:
            # If in Long hall, always show description from room dictionary
            if current_room == 'Long Hall':
                print(rooms[current_room]['desc'])
                print('Inventory: ', inventory)
                return current_room
            # Check if player has all items when villain room entered
            if current_room == 'Tugley Wood':
                validate_inventory()
                return
            # If item has been taken, show nothing
            if rooms[current_room]['item'] == 'blank':
                print('Inventory: ', inventory)
                return current_room
            # If there is an item in current room, display it too
            elif 'item' in rooms[current_room]:
                print('Look Alice! It\'s the: {}'.format(rooms[current_room]['item']))
                print('Inventory: ', inventory)
                return current_room

            else:
                return current_room

    # Identify room where game begins, initial room
    # Set current room to initial room
    # Identify valid moves and items
    # Start with empty inventory list
    initial_room = 'Long Hall'
    current_room = initial_room
    valid_moves = ['West', 'East', 'North', 'South', 'Exit']
    valid_items = ['Mushroom', 'Key', 'Oraculum', 'Shell', 'Sword', 'Hat']
    inventory = []

    # Show Instructions
    instructions()

    while True:
        # Show location/inventory/item if in room
        display_location()
        # Get player move, split and keep last word in input, then capitalize
        player_move = input('What next Alice? ').split()[-1].capitalize()
        line()

        # Error if item in already inventory
        if player_move in inventory:
            print('You already have the {}. Try again.'.format(player_move))
            line()
        # Initiate exit_game function if player types exit
        elif player_move == 'Exit':
            exit_game()
        # If player enters valid directional move, check if able to move there
        # If able to move, change current_room
        # Player must have key from rabbit's house to enter garden
        elif player_move in valid_moves:
            if player_move in rooms[current_room]:
                if current_room == 'Long Hall':
                    if player_move == 'North':
                        if 'Key' in inventory:
                            current_room = rooms[current_room][player_move]
                            print('Unlocking the door to The Garden.')
                            line()
                        else:
                            print('Cannot go {} yet.'.format(player_move))
                            print('Looks like the door to The Garden is locked.\n'
                                  '(Find the Golden Key to unlock it and try again.)')
                            line()
                    else:
                        current_room = rooms[current_room][player_move]
                else:
                    current_room = rooms[current_room][player_move]
            # Print error if unable to move in player move direction
            else:
                print('There is nothing to the {}, Alice! Try again.'.format(player_move))
                line()

        # If player enters valid item as move, check if item is in current_room
        # Add to inventory if item in current_room, print description, remove item from current_room
        # Print error if item not in current_room
        elif player_move in valid_items:
            if player_move != rooms[current_room]['item']:
                print('That item is not here, Alice. Try again.')
                line()
            if player_move in rooms[current_room]['item']:
                inventory.append(rooms[current_room]['item'])
                print('The {} has been added to your inventory!'.format(player_move))
                print(rooms[current_room]['desc'])
                line()
                rooms[current_room]['item'] = 'blank'
        # Print error if player enters invalid move
        else:
            print('What cannot be done cannot be done, Alice\nPlease enter a valid move.\n\n'
                  'Move commands: go North, go South, go East, go West\n'
                  'Collect command: get \'Item\'\nType \'Exit\' to leave the game')
            line()


main()
