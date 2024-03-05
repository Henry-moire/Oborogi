# There are 5 basic damage types and 10 effects.
# Damage types: Fire, earth, water, air, raw.
# Combinations:
# Fire - Earth = Lava/Magma
# Fire - Water = Steam
# Fire - Air = Firestorm
# Earth - Water = Mud
# Earth - Air = Sand/Dust
# Water - Air = Storm/Ice
# Effects: damage over time, stun, change stats, ignore defences, vulnerability, protection, delayed damage, summon,
# conditional(if some condition is met, nuke 'em), and transmute

class Magic:
    # attributes
    damage = 0
    damage_type = ""
    effect = {}

    def __init__(self, name, damage, effect):
        self.name = name
        self.damage = damage
        self.effect = effect

    def __getitem__(self, item):
        return self


fireball = Magic("Fireball", 10, {'dot': 2})
earthquake = Magic("Earthquake", 15, {'slow': 2})
lightning = Magic("Lightning", 8, {'lower': 2})
gale = Magic("Gale", 7, {'raise': 2})
