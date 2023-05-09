print ("Welcome dear traverler")

answer = input("Would you like to embark on this journey? (yes/no)" )
if answer.lower().strip() == "yes":
    print("Whoopy")
    print("You have fifty days to make to the Kingdom, or your your treasure will forever be lost.")
    print("Within these fifty days, you'll be tasked with diffrent choices in which will either get you to your destination or you will unfourtnly be eliminated")

class Traveler:
    def __init__ (self, name, coins):
        self.name = name 
        self.coins = coins

    def show(self):
        print("Name is:", self.name, "and amount of coins is", self.coins)

name = input("what is your name?")

User = Traveler(name, 100)
User.show()

   
answer = input("are you ready for your first choice?")
if answer.lower().strip() == "yes":
    print("")

    
else:
    print("Oh well, farrell dear traverler") 
