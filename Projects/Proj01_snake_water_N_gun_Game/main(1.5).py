# -1 for water
# 0 for gun
# 1 for snake

import random

print('Snake, Water and Gun Game')

# Computer randomly selects a choice from the predefined numerical values.
computer_chs = random.choice([-1, 0, 1])

# Prompts the user to input their choice. The input is converted to lowercase
# to ensure case-insensitivity when matching with the dictionary keys.
your_str = input('Enter your choice: ').lower()

# This dictionary maps the string representation of choices (from user input)
# to their corresponding numerical values.
Your_dict = {'snake': 1, 'water': -1, 'gun': 0}

# This dictionary provides the reverse mapping, allowing numerical values
# to be easily converted back to human-readable string representations for display.
Revs_dict = {1: 'Snake', -1: 'Water', 0: 'Gun'}

# Converts the user's string choice into its numerical representation using Your_dict.
you = Your_dict[your_str]

# Prints out both the user's choice and the computer's choice in a readable format.
print(f'You choose: {Revs_dict[you]} \nComputer choose: {Revs_dict[computer_chs]}')

# Checks if the computer's choice is the same as the user's choice, indicating a draw.
if (computer_chs == you):
    print('It\'s a Draw!')

# If it's not a draw, the game proceeds to determine the winner based on the rules.
else:
    '''
    # Condition for computer choosing water (-1).
    if (computer_chs == -1) and (you == 1): # -2 (computer_chs - you)
        print('You Win!\nSnake gulps the water')

    # Condition for computer choosing water (-1) and user choosing gun (0).
    elif (computer_chs == -1) and (you == 0): # -1 (computer_chs - you)
        print('You Lose!\nGun doesn\'t fire under water')

    # Condition for computer choosing gun (0) and user choosing snake (1).
    elif (computer_chs == 0) and (you == 1): # -1 (computer_chs - you)
        print('You Lose!\nGun killed the Snake')

    # Condition for computer choosing gun (0) and user choosing water (-1).
    elif (computer_chs == 0) and (you == -1): # 1 (computer_chs - you)
        print('You Win!\nGun failed to fire under water')

    # Condition for computer choosing snake (1) and user choosing water (-1).
    elif (computer_chs == 1) and (you == -1): # 2 (computer_chs - you)
        print('You Lose!\nSnake drank the Water')

    # Condition for computer choosing snake (1) and user choosing gun (0).
    elif (computer_chs == 1) and (you == 0): # 1 (computer_chs - you)
        print('You Win!\nGun shot the Snake dead')

    # This 'else' block will catch any combination not explicitly covered by the
    # 'if' and 'elif' statements above, indicating an unexpected scenario or error.
    else:
        print('Something went Wrong!')
    '''

    # Replaced the big if elif else block with a simple observersational pattern  <computer_chs - you>
    if (computer_chs - you == -1) or (computer_chs - you == 2): # Observing the loosing cases I discovered, for those cases (computer_chs - you) is either of [-1, 2]
        print('You Lose!')

    else:
        print('You Win!') 

