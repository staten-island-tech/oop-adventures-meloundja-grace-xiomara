print("Congrats, you've made the correct choice and you're succsefully on your way to your beloved tresure")
class Charater():
    def __init__ (self, name, coins):
        self.name = name 
        self.coins = coins

    def __str__(self):
        return f"{self.name}, {self.coins}"

class Merchant(Charater):
    def __init__ (self, name, coins, impression):
        super().__init__(name, coins,)
        self.name = name 
        self.coins = coins  
        self.impression = impression
    def __str__(self):
        return f"{self.name}, {self.coins}, {self.impression}"
    
def show(self):
        print("You've ran into a", self.name, "and his amount of coins is", self.coins, "he comes off as", self.impression)


name = "Old Merchant"
impression = "suspicious"

m = Merchant(name, 0, impression)




    
