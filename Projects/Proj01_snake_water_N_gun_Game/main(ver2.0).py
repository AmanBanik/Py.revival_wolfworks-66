import random

# Game outcomes represented numerically
# -1 for water
# 0 for gun
# 1 for snake

print('Snake, Water and Gun Game')

# Dictionary to map user string input to numerical representation
Your_dict = {'snake': 1, 'water': -1, 'gun': 0}
# Dictionary to map numerical representation back to string for display
Revs_dict = {1: 'Snake', -1: 'Water', 0: 'Gun'}

# --- Start of the loop for 9 iterations ---(Star section!)
for i in range(9): # This loop will run 9 times (for i from 0 to 8)
    print(f"\n--- Round {i + 1} ---") # Optional: to show current round number

    computer_chs = random.choice([-1, 0, 1])

    # Input validation loop
    while True:
        your_str = input('Enter your choice (snake, water, or gun): ').lower()
        if your_str in Your_dict:
            break # Exit the loop if input is valid
        else:
            print("Invalid choice. Please enter 'Snake', 'Water', or 'Gun'.")

    you = Your_dict[your_str]

    print(f'You choose: {Revs_dict[you]} \nComputer choose: {Revs_dict[computer_chs]}')

    if (computer_chs == you):
        print('It\'s a Draw!')

    else:
        # Using elif for correct logical flow
        if (computer_chs == -1) and (you == 1): # Computer: Water, You: Snake
            print('You Win!\nSnake gulps the water')
        elif (computer_chs == -1) and (you == 0): # Computer: Water, You: Gun
            print('You Lose!\nGun doesn\'t fire under water')
        elif (computer_chs == 0) and (you == 1): # Computer: Gun, You: Snake
            print('You Lose!\nGun killed the Snake')
        elif (computer_chs == 0) and (you == -1): # Computer: Gun, You: Water
            print('You Win!\nGun failed to fire under water')
        elif (computer_chs == 1) and (you == -1): # Computer: Snake, You: Water
            print('You Lose!\nSnake drank the Water')
        elif (computer_chs == 1) and (you == 0): # Computer: Snake, You: Gun
            print('You Win!\nGun shot the Snake dead')
# --- End of the loop ---

print("\nGame finished after 9 rounds!")