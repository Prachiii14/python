import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, position, snakes, ladders):
    dice_value = roll_dice()
    print(f"{player} rolled a {dice_value}")
    new_position = position + dice_value
    
    if new_position in snakes:
        print(f"Oh no! {player} got bitten by a snake at {new_position} and moves down to {snakes[new_position]}")
        return snakes[new_position]
    elif new_position in ladders:
        print(f"Great! {player} climbed a ladder from {new_position} to {ladders[new_position]}")
        return ladders[new_position]
    elif new_position > 100:
        print(f"{player} needs exactly {100 - position} to win. Try again next turn.")
        return position
    else:
        return new_position

def play_game():
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    positions = {"Player 1": 0, "Player 2": 0}
    turn = "Player 1"
    
    while True:
        input(f"{turn}'s turn. Press Enter to roll the dice...")
        positions[turn] = move_player(turn, positions[turn], snakes, ladders)
        print(f"{turn} is now at position {positions[turn]}")
        
        if positions[turn] == 100:
            print(f"Congratulations! {turn} wins the game!")
            break
        
        turn = "Player 1" if turn == "Player 2" else "Player 2"

if __name__ == "__main__":
    play_game()
