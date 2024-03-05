class Character:
    # attributes
    health = 0
    attack = 0
    defence = 0
    speed = 0
    spells = []

    def __init__(self, name, health, attack, defence, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed

    def __getitem__(self, item):
        return self
