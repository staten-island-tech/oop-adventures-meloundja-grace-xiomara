class Area():
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __str__(self):
        return f"{self.name}, {self.size}"

class Island(Area):
    def __init__(self, name, size, travel_time, description):
        super().__init__(name, size)
        self.travel_time = travel_time
        self.description = description
    def __str__(self):
        return f"{self.name}, {self.size}, {self.travel_time}, {self.description}"

island2 = Island('Siwan Bay', 'Large Island', '10 Days to Travel', '')
island3 = Island('Lost Souls Springs', 'Small Island', '20 Days to Travel', '')


island_pick = input("You are presented with these two islands to travel to. Would you like to see the information?")
if island_pick == 'Yes' or 'Y' or 'yes':
        print(island2)
        print(island3)
        pick = input('Are you ready to choose now?')
        if pick == 'Yes' or 'Y' or 'yes':
            print('Alright... Make your choice.')
        if pick == 'no' or 'No' or 'N':
            print('Please, take some time to decide....')
        else:
            print("error")
elif island_pick == 'no' or 'No' or 'N':
        print('Alright... Make your choice.')
else: 
        print('error')
