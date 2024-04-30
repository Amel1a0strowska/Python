import random

# Define a list of words for different levels
levels = {
    "easy": ["apple", "banana", "cherry", "orange", "pear"],
    "medium": ["peach", "grape", "kiwi", "melon", "plum"],
    "hard": ["dragonfruit", "guava", "mango", "papaya", "pineapple"]
}

def random_word(level):
    return random.choice(levels[level])

def check_guess(word, guess):
    if word == guess.lower():
        return True
    return False

def game(level):
    word = random_word(level)
    attempts = 3
    
    print(f"You are playing the {level} level. Guess the fruit!")
    
    while attempts > 0:
        guess = input(f"Your guess ({attempts} attempts left): ")
        
        if check_guess(word, guess):
            print("Congratulations! You guessed the word correctly! Yipee!")
            break
        else:
            print("Wrong guess. Try again.")
            attempts -= 1
            
    if attempts == 0:
        print(f"Out of attempts. The word was {word}. Better luck next time!")

def play():
    while True:
        selected_level = input("Select a level (easy, medium, hard): ")
        
        if selected_level in levels:
            game(selected_level)
        else:
            print("Invalid level selected. Please choose from easy, medium, or hard.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

play()