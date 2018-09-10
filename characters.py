class BaseCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health

    def attack(self, enemy):
        print(f'Take this {enemy.name}!')
        damage = max(0, self.get_damage() - enemy.get_defense())
        damage = min(enemy.health, damage)
        enemy.health -= damage
        print(f'Attack with {damage} damage\n')

    def get_damage(self):
        raise NotImplementedError('This is an abstract class')


class Monster(BaseCharacter):
    def __init__(self, name, health, damage, defense):
        super().__init__(name, health)
        self._damage = damage
        self._defense = defense

    def get_damage(self):
        return self._damage

    def get_defense(self):
        return self._defense


class Player(BaseCharacter):
    def __init__(self):
        super().__init__('Player', 50)
        self._strength = 10
        self._dexterity = 10
        self._agility = 10
        self._vitality = 10

        self._weapon = dict(type='Fists', damage=1)
        self._armor = dict(helmet=None, chest=None, shield=None)

    def get_damage(self):
        return self._weapon['damage'] * self._strength + self._agility

    def get_defense(self):
        return sum([a['value'] for a in self._armor.values() if a is not None])
