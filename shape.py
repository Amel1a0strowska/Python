import random

# Define a list of shapes for different levels
levels = {
    "easy": ["circle", "square", "triangle", "rectangle", "pentagon"],
    "medium": ["hexagon", "octagon", "ellipse", "parallelogram", "rhombus"],
    "hard": ["trapezoid", "heptagon", "dodecagon", "icosagon", "star"]
}

def random_shape(level):
    return random.choice(levels[level])

def check_guess(shape, guess):
    if shape == guess.lower():
        return True
    return False

def game(level):
    shape = random_shape(level)
    attempts = 3
    
    print(f"You are playing the {level} level. Guess the shape!")
    
    while attempts > 0:
        guess = input(f"Your guess ({attempts} attempts left): ")
        
        if check_guess(shape, guess):
            print("Congratulations! You guessed the shape correctly! Yipee!")
            break
        else:
            print("Wrong guess. Try again.")
            attempts -= 1
            
    if attempts == 0:
        print(f"Out of attempts. The shape was {shape}. Better luck next time!")

def play():
    while True:
        selected_level = input("Select a level (easy, medium, hard): ")
        
        if selected_level in levels:
            game(selected_level)
        else:
            print("Invalid level selected. Please choose from easy, medium, or hard.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing the shape guessing game!")
            break

play()