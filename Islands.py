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


print("You are presented with these two islands to travel to. Would you like to see the information?")
island_pick = input()
if island_pick == 'yes':
    print(island2)
    print(island3)
    choice = input("Are you ready to choose now?")
    if choice == 'yes':
        print('Alright. Make your choice now....')
        print("Type anything to continue")
        next_choice = input()
    elif choice == 'no':
        print('Alright, take some time to decide')
        print("Type anything to continue")
        next_choice = input()
    else:
        print('error')


elif island_pick == 'no':
    print("Are you sure you do not want to see the descriptions for these islands?")
    print("This is your last chance to make a descision")
    choose = input()
    if choose == 'yes':
        print('Alright. Please, make a choice now...')
        print("Type anything to continue")
        next_choice = input()
    elif choose == 'no':
        print("So, would you like to see the island descriptions")
        choose2 = input()
        if choose2 == 'yes':
            print(island2)
            print(island3)
            print('Make your choice now, please. Your decision awaits.')
            print("Type anything to continue")
            next_choice = input()
        elif choose2 == 'no':
            print("....")
            print("....")
            print("....")
            print("....")
            print("....")
            print("....")
            print("....")
            print("That was your last chance to see the island options. Make a choice now if you will")
            print("Type anything to continue")
            next_choice = input()


else:
    print('error')



for i in next_choice:
    print("Alright, your decision awaits.")
    print("Please choose between Island 2 or Island 3. Type 'two' for Island 2 and 'three for Island 3")
    island_choice_omg = input()

if island_choice_omg == "two":
    print("You have chosen Island 2")

if island_choice_omg == "three":
    print("You have chosen Island 3")