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

valid_moves = ['West', 'East', 'North', 'South', 'Exit']
valid_items = ['Mushroom', 'Key', 'Oraculum', 'Shell', 'Sword', 'Hat']


# Function to display location and inventory
def display_location(current_room, inventory):
    print('You are in {}.'.format(current_room))
    while True:
        # If in Long hall, always show description from room dictionary
        if current_room == 'Long Hall':
            print(rooms[current_room]['desc'])
            print('Inventory: ', inventory)
            return current_room
        # Check if player has all items when villain room entered
        if current_room == 'Tugley Wood':
            validate_inventory(current_room, inventory)
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


def validate_inventory(current_room, inventory):
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


def exit_game():
    while True:
        print('Are you sure you want to leave?')
        exit_command = input('Type \'Y\' to EXIT or \'N\' to RESTART: ').lower()
        if exit_command == 'n':
            return False
            # main()
        if exit_command == 'y':
            line()
            print('\nTake care Alice! See you next time!')
            return True
            # exit()
        else:
            line()
            print('Invalid response. Try again.')
            line()
            continue


def play_again():
    line()
    while True:
        print('Would you like to play again?')
        start_over = input('Type \'Y\' to RESTART or \'N\' to EXIT: ').lower()
        if start_over == 'y':
            return True
            # main()
        if start_over == 'n':
            line()
            print('\nSo long Alice! See you next time!')
            return False
            # exit()
        else:
            line()
            print('Invalid response. Try again.')
            line()
            continue


def line():
    print('-' * 75)