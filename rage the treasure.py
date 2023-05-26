#Rage the Treasure

import time
t = 1.5
t2 = 2.5
time.sleep(t)


#introduction
print ("Welcome dear traveler")

def journey():
    answer = input("Would you like to embark on this journey? (yes/no)" )
    if answer.lower().strip() == "yes":
        print("Whoopy")
        time.sleep(t)
        print("You have twenty five days to make to the Kingdom benevolent falls, or your your treasure will forever be lost.")
        time.sleep(t2)
        print("Within these twenty five days, you'll be tasked with different choices in which will either get you to your destination or you will unfortunately be eliminated")
        time.sleep(t2)
        print('remember to read each dialogue carefully, so you do not put in the wrong choice')
        first_choice()
    else:
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="No" or q=="N" or q=="n" or q=="no"):
                x = False
                break
journey()

def first_choice():  
    answer2 = input("are you ready for your first choice?")
    if answer2.lower().strip() == "yes":
        print("Ok, you are in the land of the beginning, which is where your journey starts. Unfortunately, due to your terrible luck, you are broke. Your goal is to find the treasure hidden inside the Kingdom of benevolent falls through a bunch of decisions and some might be deemed fatal.   ")
        food_optn1()
    else:
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="No" or q=="N" or q=="n" or q=="no"):
                x = False
                break



    

    #AD SOETHING HERE TATH CONECTS TO THE EXT DAY 


   

#food decision/day 5


def food_optn1():
    option = input('what would you like to bring with you on your travels? Meat is 90 gold coins and potion is 50 gold coins. They will both last 50 days of your adventure(meat/potion)')
    if option == 'meat':
        print('cost is 90 gold coins')
        choice = input('do you still want to purchase this item?')
        if choice == 'yes':
            print('you have 10 coins left')
        elif choice == 'no':
            print('Okay so you want potion instead? (yes1/no)')
            choice = input()
            if choice == 'yes1':
                print('okay you have 50 coins left and continued on your journey')
            elif choice == 'no':
                print('thank you for visiting but unfortunately you will die due to starvation on your adventure')
                choice = input()
            
            else:
                print('not a choice')
                


    elif option == 'potion':
        print('cost is 50 gold coins')
        choice = input('do you still want to purchase this item?')
        if choice == 'yes':
            print('you have 50 coins left')
        elif choice == 'no':
            print('Okay do you want meat instead? (yes2/no)')
            choice = input()
            if choice == 'yes2':
                print('okay you have 10 coins left and continued on your journey ')
            elif choice == 'no':
                print('thank you for visiting but unfortunately you will die due to starvation on your adventure')
                choice = input()


    else:
        print('not in stock')
    next_option = input()


    if next_option == 'meat' or 'yes2':
        print('This is day 5 and it is time to make a new decision. Do you want to eat the food you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
        choice = input()
        if choice == 'yes':
            print('ok, you may continue on your adventure')
            islnchoice_s()
        elif choice == 'no':
            print('You have starved to death and died. YOUR JOURNEY ENDS')




    elif next_option == 'potion' or 'yes1':
        print('This is day 5 and it is time to make a new decision. Do you want to use the potion you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
        choice = input()
        if choice == 'yes':
            print('Oops, seems like the potion you bought is poisoned so you just died ')
        elif choice == 'no':
            print('You have starved to death and died. YOUR JOURNEY ENDS')

#Day 10
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



def islnchoice_s():
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
        print("This is your last chance to make a decision")
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
        print()
    


    print("Alright, your decision awaits.")
    print("Please choose between Island 2 or Island 3. Type '2' for Island 2 and '3' for Island 3")
    island_choice_omg = input()
    if island_choice_omg == '2':
        print("You have chosen Island 2")


    elif island_choice_omg == '3':
        print("You have chosen Island 3")


    else:
        print('error')

#Day15
def day15fnl():
    print("congrats dear traveler, you've made it to day 15 and you have cosen island 2!")
    print("an important choice awaits, choose wisly...")
    print("you must choose between giving up ownership of either you gold coins or your items")


    choice = input("what are you willing to give up? gold coins or items?")


    if choice == "gold coins":
        print("unfortunately  this island is a death sentence, lack of coins or items guarantee death")


    elif choice == "items":
        print("unfortunately  this island is a death sentence, lack of items or coins guarantee death")


    print("game over")


    from time import sleep
    print("Congrats, you've made the correct choice and you're successfully on your way to your beloved treasure")
    class Character():
        def __init__ (self, name, coins):
            self.name = name
            self.coins = coins


        def __str__(self):
            return f"{self.name}, {self.coins}"
    x = 2
    class Merchant(Character):
        def __init__ (self, name, coins, impression):
            super().__init__(name, coins,)
            self.name = name
            self.coins = coins  
            self.impression = impression
    
            print("You've ran into a",self.name,"and his amount of coins is", self.coins, "he comes off as", self.impression)
            sleep(x)




    name = "Old Merchant"
    impression = "suspicious"


    m = Merchant(name, 0, impression)


    print("The merchant promises to gain you access to the island in four days, do you believe him?")
    sleep(x)


    choice = input("Do you agree?")
    sleep(1)


    if choice == "yes" or "Y" or "y":
        print("you've made a horrible choice, you've been tricked and now you'll die")
        sleep(1)


    elif choice == "no" or "N" or "n":
        print("Congrats, he is a horrible trickster and you've just avoided death!")


    else:
        print("error")

#Day 20

#Day25

last_choice = input('You just arrived at the kingdom of island 4, and here sits the treasure chest that you have long awaited. Would you like to open the chest or go home? (open chest/ go home) ')


if last_choice == 'go home':
    print('Ok guess all that work was for nothing. Your journey....')
    time.sleep(t)
    print("ENDS!!!!")
    time.sleep(t)
    print('Sorry that you suck at this game, but thanks for playing anyway ;) BYE!')


   
elif last_choice == 'open chest':
    print('There is the long awaited treasure you have longed for that will make you rich... HUH all you see is a few cabbages and a note inside. Would you like to read the note? (sure/nah)')


else:
        print('not a choice. take this game seriously and put in the right choice')
read_letter = input()


if read_letter == 'sure':
        print('Unfortunately you have failed the test. Due to your greediness, you even ditched the 1000 gold coins. Instead of donating the money to charity you failed. To make you feel better, here are some cabbages as a gift for your long journey.')
        time.sleep(t)
        print('Thanks for playing this awesome rage quitting game. Hope you have a good day. Goodbye')


elif read_letter == 'nah':
        print('well guess you go home with your cabbage without knowing why there is no treasure in it and starve to death because you are a brokie.')
        time.sleep(t)
        print('Thanks for playing. BYE BYE!!!')


else:
        print('not a choice. take this game seriously and put in the right choice by reading the instructions')









