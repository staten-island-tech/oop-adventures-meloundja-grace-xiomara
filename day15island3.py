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
 
    
        print("You've ran into a",self.name,"and his amount of coins is", self.coins, "he comes off as", self.impression)


name = "Old Merchant"
impression = "suspicious"

m = Merchant(name, 0, impression)

print("The merchant promises to gain you accses to the island in four days, do you belive him?")

choice = input("Do you agree?")

if choice == "yes" or "Y" or "y":
    print("you've made a horrible choice, you've been tricked and now you'll die")

elif choice == "no" or "N" or "n":
    print("Congrats, he is a horribble trickster and you've just avoided death!")

else:
    print("error")



    
