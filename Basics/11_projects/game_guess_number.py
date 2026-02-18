import random


def play_game():
    random_number = random.randint(1, 100)
    user_guess = -1
    attempt_count = 1
    while user_guess != random_number:
        user_guess = int(input(f"Guess the Number: "))
        if user_guess > random_number:
            print("\t\tChoose a Lower number")
            attempt_count += 1
        elif user_guess < random_number:
            print("\t\tChoose a Higher number")
            attempt_count += 1
        else:
            break
    return attempt_count


def multiplayer_game():
    guess_results = {}
    for player_index in range(2):
        guessed_attempts = play_game()
        print(f"Player {player_index + 1} Guessed in {guessed_attempts} attempt\n")
        guess_results[f"Player {player_index}"] = guessed_attempts

    if guess_results["Player 0"] == guess_results["Player 1"]:
        print("Match Draw")
    elif guess_results["Player 0"] > guess_results["Player 1"]:
        print("Player 2 Won")
    elif guess_results["Player 0"] < guess_results["Player 1"]:
        print("Player 1 Won")
    else:
        print("Something Wrong Happen!")


multiplayer_game()
