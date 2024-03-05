import random
import UI


def turn_order(player_stats, enemy_stats, player_input):
    if player_stats.speed >= enemy_stats.speed:
        player_action(player_stats, enemy_stats, player_input)
        if health_check(enemy_stats):
            return
        enemy_action(player_stats, enemy_stats)
        if health_check(player_stats):
            return
    else:
        enemy_action(player_stats, enemy_stats)
        if health_check(player_stats):
            return
        player_action(player_stats, enemy_stats, player_input)
        if health_check(enemy_stats):
            return


def health_check(actor):
    if actor.health <= 0:
        return True
    else:
        return False


def enemy_action(player_stats, enemy_stats):
    action = random.randint(1, 1)
    if action == 1:
        damage = enemy_stats.attack - player_stats.defence
        if damage < 0:
            damage = 0
        print(f'The {enemy_stats.name} deals {damage} damage.')
        player_stats.health -= damage

    elif action == 2:
        print("The enemy stares at you, menacingly!")


def player_action(player_stats, enemy_stats, player_input):
    if player_input == 1:
        damage = (player_stats.spells[0].damage + player_stats.attack) - enemy_stats.defence
        print(f'You deal {damage} damage.')
        enemy_stats.health -= damage
        secondary_effects(player_stats, enemy_stats, player_stats.spells[0].effect)
        print(f' Your attack is {player_stats.attack}')
    elif player_input == 0:
        print("You run away!")
        UI.title_screen()


# The game should begin/end the turn by checking for any active effects. If any, apply them, then reduce the timer by 1
def secondary_effects(player_stats, enemy_stats, effect):
    if effect is not None:
        if 'dot' in effect:
            print("Damage over time")
            damage = effect['dot']
            print(f'The fire burns for {damage} damage.')
            enemy_stats.health -= damage
        elif 'slow' in effect:
            print("Slow")
            damage = effect['slow']
            print(f'The enemy is slowed by {damage}.')
            enemy_stats.speed -= damage
        elif 'lower' in effect:
            print("Lower stats")
            damage = effect['lower']
            print(f'The enemy is attack is lowered by {damage}.')
            enemy_stats.attack -= damage
        elif 'raise' in effect:
            print("Raise stats")
            damage = effect['raise']
            print(f'Your attack raises by {damage}.')
            player_stats.attack += damage
