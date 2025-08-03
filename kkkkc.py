import random

# Define the snake and ladder positions
snake = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladder = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Game setup
def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_position = 0
    moves = 0
    while player_position < 100:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"Dice rolled: {dice_roll}")
        
        player_position += dice_roll
        
        # Check if the player landed on a snake
        if player_position in snake:
            print(f"Oh no! You landed on a snake! Moving from {player_position} to {snake[player_position]}")
            player_position = snake[player_position]
        
        # Check if the player landed on a ladder
        elif player_position in ladder:
            print(f"Yay! You landed on a ladder! Climbing from {player_position} to {ladder[player_position]}")
            player_position = ladder[player_position]
        
        # Check for a winning condition
        if player_position > 100:
            player_position = 100
        
        print(f"Your current position is {player_position}")
        moves += 1
        
        if player_position == 100:
            print(f"Congratulations! You've won the game in {moves} moves.")
            break

# Start the game
play_game()
