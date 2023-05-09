class item():
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def __str__(self):
        return f"{self.name}, {self.cost}"

class Food(item):
    def __init__(self, name, cost, stats):
        super().__init__(name, cost)
        self.stats = stats
    def __str__(self):
        return f"{self.name}, {self.cost}, {self.stats}"

class Potion(item):
    def __init__(self, name, cost, type, description):
        super().__init__(name, cost)
        self.type = type
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.cost}, {self.type}, {self.description}"

food = Food("Meat", "90 Gold Coins", "(Lasts all 30 days)")
print(food)

potion = Potion("HPotion", "50 Gold Coins", "Hunger", "Description: A mysterious potion that appears to be able to relieve hunger. You can see a tag on it that says 'PROPERTY OF BLACK MARKET'.")
print (potion)