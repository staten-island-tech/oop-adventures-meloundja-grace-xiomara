#CHARACTERS
class Character():
    def __init__ (self, name, coins):
        self.name = name
        self.coins = coins



    def __str__(self):
        return f"{self.name}, {self.coins}"

class Merchant(Character):
    def __init__ (self, name, coins, impression):
        super().__init__(name, coins,)
        self.name = name
        self.coins = coins  
        self.impression = impression
    
    def __str__(self):
        return f"{self.name}, {self.coins}, {self.impression}"





