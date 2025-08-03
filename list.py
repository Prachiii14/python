import time
import re
import random
from datetime import datetime

REGISTRATION_TIME = 10  
MIN_PARTICIPANTS = 3
LOG_FILE = "lottery_log.txt"

registered_users = {}

def is_valid_username(username):
    return bool(re.fullmatch(r'[A-Za-z0-9_]{3,15}', username))

def registration_phase():
    print(f"Registration started! You have {REGISTRATION_TIME} seconds.")
    start_time = time.time()
    end_time = start_time + REGISTRATION_TIME
    
    while time.time() < end_time:
        remaining = int(end_time - time.time())
        print(f"\n Time left: {remaining}s")
        username = input("Enter username to register: ").strip()

        if not is_valid_username(username):
            print("Invalid username! Use 3–15 letters/numbers/underscores only.")
            continue
        if username in registered_users:
            print("Username already registered.")
            continue

        registered_users[username] = time.time()
        print(f"Registered: {username}")

    print("\n Registration time is over!")
    return list(registered_users.keys()), start_time

def show_results(participants):
    random.shuffle(participants)
    print("\n Lottery Results:")
    results = []
    for i, name in enumerate(participants, start=1):
        print(f"Rank {i}: {name}")
        results.append((i, name))
    return results

def log_results(results, start_time, winner):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("Lottery Log\n")
        f.write(f"Start Time: {datetime.fromtimestamp(start_time)}\n")
        f.write("Participants:\n")
        for user, ts in registered_users.items():
            f.write(f" - {user} (registered at {datetime.fromtimestamp(ts)})\n")

        f.write("\n Lottery Results:\n")
        for rank, username in results:
            f.write(f"Rank {rank}: {username}\n")

        f.write(f"\n Winner: {winner}\n")
        f.write(f"Total Participants: {len(registered_users)}\n")
        f.write("-" * 50 + "\n")

def main():
    participants, start_time = registration_phase()
    
    if len(participants) < MIN_PARTICIPANTS:
        print(f"\n Not enough participants! Minimum required is {MIN_PARTICIPANTS}.")
        return

    results = show_results(participants)
    winner = results[0][1]  
    log_results(results, start_time, winner)

    print(f"\n Congratulations, {winner}     You are the **WINNER** of this lottery round.")

    print(f"Results and winner details saved to '{LOG_FILE}'.")

if __name__ == "__main__":
    main()