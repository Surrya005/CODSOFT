import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    ties = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
            ties += 1
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        print(f"\nScore:\nYou: {user_score} | Computer: {computer_score} | Ties: {ties}")
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("\nThank you for playing! Final score:")
    print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    print("Goodbye!")

if __name__ == "__main__":
    main()
