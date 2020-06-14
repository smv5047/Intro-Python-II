class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description}'


class Sword(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power

    def __str__(self):
        return f'{self.name}'


class Shield(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

    def __str__(self):
        return f'{self.name}'
