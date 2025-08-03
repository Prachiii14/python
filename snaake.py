import random

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice_value):
    position += dice_value
    if position in snakes:
        print(f"Oh no! A snake! Moved down from {position} to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Great! A ladder! Climbed up from {position} to {ladders[position]}")
        position = ladders[position]
    return position

def play_game():
    player_positions = {1: 0, 2: 0}
    turn = 1
    while True:
        input(f"Player {turn}, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"Player {turn} rolled a {dice_value}")
        new_position = move_player(player_positions[turn], dice_value)
        print(f"Player {turn} moved to {new_position}\n")
        
        if new_position >= 100:
            print(f"Congratulations! Player {turn} wins!")
            break
        
        player_positions[turn] = new_position
        turn = 2 if turn == 1 else 1

snakes = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

ladders = {
    3: 22,
    6: 25,
    11: 40,
    20: 38,
    27: 84,
    39: 58,
    50: 67,
    63: 81,
    72: 91
}

if __name__ == "__main__":
    print("Welcome to Snake and Ladder! Two players will take turns to roll the dice.")
    play_game()
