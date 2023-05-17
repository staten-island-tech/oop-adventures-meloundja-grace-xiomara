print("Congrats, you've made the correct choice and you're succsefully on your way to your beloved tresure")

class Merchant():
    def __init__ (self, suspicious):
        self.suspicious = suspicious
    def __str__(self):
        return f"{self.suspicious}"    
    
print(f"You've ran into a Merchant")
