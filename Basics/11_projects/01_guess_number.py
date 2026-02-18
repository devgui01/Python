"""
Guess the Number Game - Multiplayer

A number guessing game where players compete to guess the number in fewer attempts.
"""
import random


def get_valid_input(prompt: str) -> int:
    """Get validated integer input from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")


def game(min_num: int = 1, max_num: int = 100) -> int:
    """
    Play the guessing game.
    
    Args:
        min_num: Minimum number for the range
        max_num: Maximum number for the range
    
    Returns:
        Number of attempts taken to guess correctly
    """
    random_number = random.randint(min_num, max_num)
    user_input = -1
    guess = 1
    
    print(f"\n🎯 Guess the number between {min_num} and {max_num}!")
    
    while user_input != random_number:
        user_input = get_valid_input(f"Attempt {guess} - Your guess: ")
        
        if user_input > random_number:
            print("\t📉 Choose a LOWER number")
            guess += 1
        elif user_input < random_number:
            print("\t📈 Choose a HIGHER number")
            guess += 1
    
    print(f"✅ Correct! You guessed it in {guess} attempts!")
    return guess


def Multiplayer():
    """Play multiplayer mode with 2 players."""
    print("=" * 50)
    print("🎮 MULTIPLAYER GUESS THE NUMBER 🎮")
    print("=" * 50)
    
    # Get game settings
    try:
        min_num = get_valid_input("Enter minimum number (e.g., 1): ")
        max_num = get_valid_input("Enter maximum number (e.g., 100): ")
        
        if min_num >= max_num:
            print("❌ Invalid range! Using default 1-100")
            min_num, max_num = 1, 100
    except Exception:
        print("⚠️ Using default range 1-100")
        min_num, max_num = 1, 100
    
    guess = {}
    
    for player_index in range(2):
        print(f"\n{'=' * 50}")
        print(f"👤 Player {player_index + 1}'s Turn!")
        print(f"{'=' * 50}")
        guessed_val = game(min_num, max_num)
        guess[f"Player {player_index}"] = guessed_val

    # Determine winner
    print(f"\n{'=' * 50}")
    print("🏆 RESULTS 🏆")
    print(f"{'=' * 50}")
    print(f"Player 1 took {guess['Player 0']} attempts")
    print(f"Player 2 took {guess['Player 1']} attempts")
    print()
    
    if guess["Player 0"] == guess["Player 1"]:
        print("🤝 Match Draw!")
    elif guess["Player 0"] > guess["Player 1"]:
        print("🎉 Player 2 Wins!")
    elif guess["Player 0"] < guess["Player 1"]:
        print("🎉 Player 1 Wins!")
    else:
        print("⚠️ Something went wrong!")


if __name__ == "__main__":
    Multiplayer()
