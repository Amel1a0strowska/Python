# Ask the player for their name
player_name = input("What's your name adventurer? ")

# Ask the player for the name of the island
island_name = input("Welcome explorer! What would you like to name this island? ")

# Personalized greeting message
print(f"Welcome to {island_name}, {player_name}!")
print("Get ready for an adventure where every code tells a story.")

# Constants for HP and Damage
player_hp = 100
companion_hp = 100
enemy_river_hp = 50
enemy_forest_hp = 50

sword_shield_damage = 20
cloak_damage = 10
slingshot_damage = 20
attacked_with_sword_shield = 5
attacked_with_slingshot = 5
attacked_with_cloak = 5

current_player = player_name
current_player_hp = player_hp
current_player_item = ""
enemy_hp = 0

def player_attack():
    global enemy_hp
    print(f"{current_player} attacks the enemy with {current_player_item} and causes {get_damage_value()} HP of damage.")
    enemy_hp -= get_damage_value()

def get_damage_value():
    if current_player_item == "sword and shield":
        return sword_shield_damage
    elif current_player_item == "slingshot":
        return slingshot_damage
    elif current_player_item == "cloak":
        return cloak_damage
    else:
        return 0

def take_damage():
    global current_player_hp
    current_player_hp -= 5
    print(f"{current_player} skipped their attack! The enemy attacks back and causes an extra 5 HP damage. Current HP: {current_player_hp}")

def switch_player():
def run_attack_simulation():
    global enemy_hp
    while player_hp > 0 and companion_hp > 0:
        decision = input(f"{current_player}, it's your turn. Attack or Skip? (attack/skip): ")
        if decision.lower() == "attack":
            player_attack()
        elif decision.lower() == "skip":
            take_damage()
        else:
            print("Invalid input. Please choose attack or skip.")
            continue
        if enemy_hp <= 0:
            print(f"You have defeated the enemy! Congratulations!")
            break
        
        # Companion's turn
        decision = input(f"{current_player}, it's your companion's turn. Attack or Skip? (attack/skip): ")
        if decision.lower() == "attack":
            player_attack()
            print(f"{companion_name} attacks the enemy with {current_player_item} and causes {get_damage_value()} HP of damage.")
            enemy_hp -= get_damage_value()
        elif decision.lower() == "skip":
            take_damage()
            print(f"{companion_name} skipped their attack! The enemy attacks back and causes an extra 5 HP damage. Current HP: {companion_hp}")
        else:
            print("Invalid input for companion. Please choose attack or skip.")
            continue
        
        if player_hp <= 0:
            print(f"{player_name} has lost the game. Game Over.")
            break
        if companion_hp <= 0:
            print(f"{companion_name} has lost the game. Game Over.")
            break:
    global current_player
    global current_player_hp
    global current_player_item
    if current_player == player_name:
        current_player = companion_name
        current_player_hp = companion_hp
        current_player_item = companion_item
    else:
        current_player = player_name
        current_player_hp = player_hp
        current_player_item = player_item

