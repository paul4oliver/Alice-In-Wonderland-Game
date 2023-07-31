import game


# Display instructions along with commands
def instructions():
    game.line()
    print('Welcome to the Alice in Wonderland Text Game!')
    game.line()
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
    game.line()


# Main game function:
def main():
    # Identify room where game begins, initial room
    # Set current room to initial room
    # Identify valid moves and items
    # Start with empty inventory list
    initial_room = 'Long Hall'
    current_room = initial_room
    inventory = []

    # Show Instructions
    instructions()

    while True:
        # Show location/inventory/item if in room
        game.display_location(current_room, inventory)
        # Get player move, split and keep last word in input, then capitalize
        player_move = input('What next Alice? ').split()[-1].capitalize()
        game.line()

        # Error if item in already inventory
        if player_move in inventory:
            print('You already have the {}. Try again.'.format(player_move))
            game.line()
        # Initiate exit_game function if player types exit
        elif player_move == 'Exit':
            game.exit_game()
        # If player enters valid directional move, check if able to move there
        # If able to move, change current_room
        # Player must have key from rabbit's house to enter garden
        elif player_move in game.valid_moves:
            if player_move in game.rooms[current_room]:
                if current_room == 'Long Hall':
                    if player_move == 'North':
                        if 'Key' in inventory:
                            current_room = game.rooms[current_room][player_move]
                            print('Unlocking the door to The Garden.')
                            game.line()
                        else:
                            print('Cannot go {} yet.'.format(player_move))
                            print('Looks like the door to The Garden is locked.\n'
                                  '(Find the Golden Key to unlock it and try again.)')
                            game.line()
                    else:
                        current_room = game.rooms[current_room][player_move]
                else:
                    current_room = game.rooms[current_room][player_move]
            # Print error if unable to move in player move direction
            else:
                print('There is nothing to the {}, Alice! Try again.'.format(player_move))
                game.line()

        # If player enters valid item as move, check if item is in current_room
        # Add to inventory if item in current_room, print description, remove item from current_room
        # Print error if item not in current_room
        elif player_move in game.valid_items:
            if player_move != game.rooms[current_room]['item']:
                print('That item is not here, Alice. Try again.')
                game.line()
            if player_move in game.rooms[current_room]['item']:
                inventory.append(game.rooms[current_room]['item'])
                print('The {} has been added to your inventory!'.format(player_move))
                print(game.rooms[current_room]['desc'])
                game.line()
                game.rooms[current_room]['item'] = 'blank'
        # Print error if player enters invalid move
        else:
            print('What cannot be done cannot be done, Alice\nPlease enter a valid move.\n\n'
                  'Move commands: go North, go South, go East, go West\n'
                  'Collect command: get \'Item\'\nType \'Exit\' to leave the game')
            game.line()


main()
