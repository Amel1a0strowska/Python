'''import time

def get_current_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    return current_time

try:
    while True:
        current_time = get_current_time()
        print(f"\r{current_time}", end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")'''

'''import random

# Define colors and their RGB values
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "orange": (255, 165, 0),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42)
}

def random_color():
    return random.choice(list(colors.keys()))

def check_guess(color, guess):
    if color == guess.lower():
        return True
    return False

def game():
    color = random_color()
    rgb_value = colors[color]
    
    print(f"RGB Value: {rgb_value}")
    
    guess = input("Guess the color: ")
    
    if check_guess(color, guess):
        print("Congratulations! You guessed the color correctly!")
    else:
        print(f"Wrong guess. The color was {color}.")

game()'''

'''import random

# Define a list of words to guess
words = ["apple", "banana", "cherry", "orange", "pear", "peach", "grape", "kiwi", "melon", "plum", "dragonfruit", "guava", "mango"]

def random_word():
    return random.choice(words)

def check_guess(word, guess):
    if word == guess.lower():
        return True
    return False

def game():
    word = random_word()
    
    print("Guess the fruit!")
    
    guess = input("Your guess: ")
    
    if check_guess(word, guess):
        print("Congratulations! You guessed the word correctly!Yipee!")
    else:
        print(f"Wrong guess. The word was {word}.Try again :(")

game()'''

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