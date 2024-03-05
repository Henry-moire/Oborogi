import character
import combat
import random
import magic


def title_screen():
    print("Welcome to the Engoro!")
    print("1. New Game")
    print("2. Exit")
    while True:
        while True:
            try:
                player_action = int(input("Enter your action: "))
            except ValueError:
                print("Invalid input. Please enter the number corresponding to the desired action.")
            else:
                break
        if player_action >= 3 or player_action <= 0:
            print("Invalid input. Please enter the number corresponding to the desired action.")
        else:
            break
    if player_action == 1:
        story()
    elif player_action == 2:
        exit()


def story():
    print("Welcome to the world of Engoro!")
    # Create the player character
    player = character.Character("player", 50, 10, 10, 10)
    # The player is randomly assigned an element and corresponding magic.
    core_magic = random.randint(1, 4)
    if core_magic == 1:
        print("You have felt an affinity to fire from the beginning.\n")
        player.spells.append(magic.fireball)
    elif core_magic == 2:
        print("You have felt an affinity to the earth from the beginning.\n")
        player.spells.append(magic.earthquake)
    elif core_magic == 3:
        print("You have felt an affinity to lightning from the beginning.\n")
        player.spells.append(magic.lightning)
    elif core_magic == 4:
        print("You have felt an affinity to the wind from the beginning.\n")
        player.spells.append(magic.gale)

    # Create the first enemy, a goblin
    print("You come across a goblin. Prepare to fight!")
    goblin = character.Character("Goblin", 20, 11, 5, 9)

    # Begin battle against the enemy
    battle_screen(player, goblin)
    # Upon winning the players stats are increased
    player = character.Character("player", 50, 15, 10, 10)
    print("You have won!")

    # Battle against the second enemy
    print("You come across a bigger goblin. Prepare to fight!")
    bigger_goblin = character.Character("Bigger Goblin", 20, 16, 10, 9)
    battle_screen(player, bigger_goblin)
    print("You have won, again!")


def battle_screen(player_stats, enemy_stats):
    while enemy_stats.health > 0 and player_stats.health > 0:
        action_count = 1
        print(f'{enemy_stats.name} health: {enemy_stats.health}')
        print("")
        print(f'Your health: {player_stats.health}')
        print("Choose an action:")
        for x in range(len(player_stats.spells)):
            print(f'{action_count}: {player_stats.spells[x].name}')
            action_count += 1
        print("0. Forfeit")
        # Input validation
        while True:
            while True:
                try:
                    player_action = int(input("Enter your action: "))
                except ValueError:
                    print("Invalid input. Please enter the number corresponding to the desired action.")
                else:
                    break
            if player_action >= action_count:
                print("Invalid input. Please enter the number corresponding to the desired action.")
            else:
                break
        combat.turn_order(player_stats, enemy_stats, player_action)
    if enemy_stats.health <= 0:
        return
    elif player_stats.health <= 0:
        print("You have lost.")
        title_screen()
