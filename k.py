import random
import time

def roll_dice():
    input("Press Enter to roll the dice...")
    dice_value = random.randint(1, 6)
    print(f"🎲 You rolled a {dice_value}")
    time.sleep(1)
    return dice_value

def move_player(player, position, snakes, ladders):
    dice_value = roll_dice()
    new_position = position + dice_value
    print(f"{player} moves from {position} to {new_position}")
    time.sleep(1)
    
    if new_position in snakes:
        print(f"🐍 Oh no! {player} got bitten by a snake at {new_position} and slides down to {snakes[new_position]}")
        time.sleep(1)
        return snakes[new_position]
    elif new_position in ladders:
        print(f"🪜 Great! {player} climbed a ladder from {new_position} to {ladders[new_position]}")
        time.sleep(1)
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
    
    print("🎲 Welcome to Snakes & Ladders! 🎲")
    print("First player to reach exactly 100 wins!")
    print("Snakes 🐍 will pull you down, ladders 🪜 will take you up. Good luck!\n")
    
    while True:
        print(f"\n{turn}'s turn! 🎲")
        positions[turn] = move_player(turn, positions[turn], snakes, ladders)
        print(f"{turn} is now at position {positions[turn]}")
        
        if positions[turn] == 100:
            print(f"🎉🎉 Congratulations! {turn} wins the game! 🎉🎉")
            break
        
        turn = "Player 1" if turn == "Player 2" else "Player 2"

if __name__ == "__main__":
    play_game()
