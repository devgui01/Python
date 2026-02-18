"""
Rock Paper Scissors Game

Classic game against the computer with input validation.
"""
import random


def get_valid_choice() -> str:
    """Get validated user input for rock/paper/scissors."""
    valid_choices = ["R", "P", "S"]
    choices_full = {"R": "Rock", "P": "Paper", "S": "Scissor"}
    
    while True:
        user_input = input("\nChoose your move:\n  [R]ock\n  [P]aper\n  [S]cissor\n\nYour choice: ").upper()
        
        if user_input in valid_choices:
            return user_input
        else:
            print(f"❌ Invalid choice! Please choose R, P, or S.")
            print(f"   You chose: '{user_input}'")


def get_winner(user: str, computer: str) -> str:
    """
    Determine the winner of Rock Paper Scissors.
    
    Args:
        user: User's choice (R, P, or S)
        computer: Computer's choice (R, P, or S)
    
    Returns:
        'win' if user wins, 'lose' if user loses, 'draw' for tie
    """
    if user == computer:
        return "draw"
    
    # Winning combinations for user
    winning_combos = [
        ("R", "S"),  # Rock beats Scissor
        ("P", "R"),  # Paper beats Rock
        ("S", "P"),  # Scissor beats Paper
    ]
    
    if (user, computer) in winning_combos:
        return "win"
    else:
        return "lose"


def play_game() -> str:
    """
    Play one round of Rock Paper Scissors.
    
    Returns:
        Game result message
    """
    choices_dict = {"R": "Rock", "P": "Paper", "S": "Scissor"}
    
    # Get validated user input
    user_choice = get_valid_choice()
    computer_choice = random.choice(["R", "P", "S"])
    
    # Display choices
    print(f"\n💭 You chose:     {choices_dict[user_choice]}")
    print(f"🤖 Computer chose: {choices_dict[computer_choice]}")
    
    # Determine result
    result = get_winner(user_choice, computer_choice)
    
    if result == "draw":
        output = "🤝 It's a Draw!"
    elif result == "win":
        output = "🎉 You Won!"
    else:
        output = "😞 You Lose, Try Again!"
    
    return output


def main():
    """Main game loop."""
    print("=" * 50)
    print("🎮 ROCK PAPER SCISSORS 🎮")
    print("=" * 50)
    
    score = {"win": 0, "lose": 0, "draw": 0}
    
    while True:
        result = play_game()
        print(f"\n{result}")
        
        # Update score
        if "Won" in result:
            score["win"] += 1
        elif "Lose" in result:
            score["lose"] += 1
        else:
            score["draw"] += 1
        
        # Display score
        print(f"\n📊 Score - Wins: {score['win']} | Losses: {score['lose']} | Draws: {score['draw']}")
        
        # Ask to play again
        play_again = input("\nPlay again? [Y/N]: ").upper()
        if play_again != "Y":
            break
    
    # Final results
    print("\n" + "=" * 50)
    print("🏆 FINAL RESULTS 🏆")
    print("=" * 50)
    print(f"Wins:   {score['win']}")
    print(f"Losses: {score['lose']}")
    print(f"Draws:  {score['draw']}")
    print(f"Total games: {sum(score.values())}")
    print("\nThanks for playing! 👋")


if __name__ == "__main__":
    main()
