#Rage the Treasure




import time
t = 1
t2 = 2
time.sleep(t)
















def first_choice():  
    answer2 = input("are you ready for your first choice?")
    if answer2.lower().strip() == "yes":
        print("Ok, you are in the land of the beginning, which is where your journey starts. Unfortunately, due to your terrible luck, you are broke. Your goal is to find the treasure hidden inside the Kingdom of benevolent falls through a bunch of decisions and some might be deemed fatal.   ")
        food_optn1()
    else:
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return first_choice()












   




    #AD SOETHING HERE TATH CONECTS TO THE EXT DAY
    #added :)








   




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
                x = True
                while x == True:
                    q = input("Would you like to continue? Y/N: ")
                    if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                        x = False
                        return food_optn1()
                   








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
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return food_optn1()
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
            time.sleep(t)
            print("Type anything to continue")
            next_choice = input()
        elif choice == 'no':
            print('Alright, take some time to decide')
            time.sleep(t)
            print("Type anything to continue")
            next_choice = input()
        else:
            print('error')
            x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return islnchoice_s()
















    elif island_pick == 'no':
        print("Are you sure you do not want to see the descriptions for these islands?")
        time.sleep(t)
        print("This is your last chance to make a decision")
        choose = input()
        if choose == 'yes':
            print('Alright. Please, make a choice now...')
            time.sleep(t)
            print("Type anything to continue")
            next_choice = input()
        elif choose == 'no':
            print("So, would you like to see the island descriptions")
            choose2 = input()
            if choose2 == 'yes':
                print(island2)
                print(island3)
                print('Make your choice now, please. Your decision awaits.')
                time.sleep(t)
                print("Type anything to continue")
                next_choice = input()
            elif choose2 == 'no':
                print("....")
                time.sleep(t)
                print("....")
                time.sleep(t)
                print("....")
                time.sleep(t)
                print("....")
                time.sleep(t)
                print("....")
                time.sleep(t)
                print("....")
                time.sleep(t)
                print("....")
                time.sleep(t)
                print("That was your last chance to see the island options. Make a choice now if you will")
                time.sleep(t)
                print("Type anything to continue")
                next_choice = input()












    else:
        print('error')
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return islnchoice_s()
















    for i in next_choice:
        print()
   








    print("Alright, your decision awaits.")
    time.sleep(t)
    print("Please choose between Island 2 or Island 3. Type '2' for Island 2 and '3' for Island 3")
    island_choice_omg = input()
    if island_choice_omg == '2':
        print("You have chosen Island 2")
        day15fnl2()








    elif island_choice_omg == '3':
        print("You have chosen Island 3")
        day15fnl3()
   








    else:
        print('error')
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return islnchoice_s()




#Day15
def day15fnl2():
    print("congrats dear traveler, you've made it to day 15 and you have chosen island 2!")
    time.sleep(t)
    print("an important choice awaits, choose wisely...")
    time.sleep(t)
    print("you must choose between giving up ownership of either you gold coins or your items")








    choice = input("what are you willing to give up? gold coins or items?")








    if choice == "gold coins":
        print("unfortunately  this island is a death sentence, lack of coins or items guarantee death")








    elif choice == "items":
        print("unfortunately  this island is a death sentence, lack of items or coins guarantee death")


    else:
        print("Error")
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return day15fnl2()








    print("game over")




def day15fnl3():
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








    choice = input("yes/no")
    sleep(1)








    if choice == "yes":
        print("you've made a horrible choice, you've been tricked and now you'll die")
        sleep(1)








    elif choice == "no":
        print("Congrats, he is a horrible trickster and you've just avoided death!")
        DAY_20()








    else:
        print("error")
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return day15fnl3()








#Day 20 (yayyy....  :| )








def DAY_20():




    ###
    def CT_Game ():
        print('Type K to continue')
        ulitmate_choice = input()
        if ulitmate_choice == "K":
            print('')
            print("Do you want to take this treasure chest with you? Or would you like to donate it to charity?")
            time.sleep(t)
            print("T for Treasure Chest and C to donate to charity.")
            supr_chiice = input()
            if supr_chiice == 'T':
                print('You chose to open the treasure chest')
                TAKE_ALL()
            elif supr_chiice == 'C':
                print('You have chose to donate to charity')
                CHARITY_W ()
            else:
                print('Error')
                x = True
                while x == True:
                    q = input("Would you like to continue? Y/N: ")
                    if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                        x = False
                        return CT_Game()
        else:
            print('Error')
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return CT_Game()
       
























    def Continue_Gmae():
        print("type J to continue")
        anther_ultimte_chpice = input()
        if anther_ultimte_chpice == "J":
            print('')
            print("Are you going to continue on your journey? You will abandon the chest.")
            mega_choice = input()
            if mega_choice == 'yes':
                print("Alright. You proceed on your journey. Good luck on your travels!!")
                LAST_DAY_YAYY()
            elif mega_choice == 'no':
                print("Too bad you're going anyways.")
            else:
                print('Error')
                x = True
                while x == True:
                    q = input("Would you like to continue? Y/N: ")
                    if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                        x = False
                        return Continue_Gmae()
        else:
            print('Error')
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return Continue_Gmae()
       








    def CHARITY_W ():
        print("OMG SO U HAVE CHOSEN TO DONATE TO CHARITY???")
        time.sleep(t)
        print("That is so kind of you!! Lets see what your fate will be.... ")
        time.sleep(t2)
        #add slep thing
        print(" Because you have chosen to donate to charity, the king and queen were impressed by your generosity. ")
        time.sleep(t)
        print("As a result... they have chosen to give you 1000000 gold coins")
        time.sleep(t)
        print("CONGRATSS YOU HAVE ACHIEVED THE BEST ENDING IN THIS GAME!!")
        time.sleep(t)
        print("END")








    def TAKE_ALL():
        print("SO U HAVE CHOSEN TO TAKE THIS TREASURE FOR YOURSELF???")
        time.sleep(t)
        print("That is..... interesting ")
        time.sleep(t2)
        print("Lets see what fate has in store for you.....")
        time.sleep(t2)
        print("You end your journey after taking the treasure chest with you")
        time.sleep(t)
        print("You wonder what your life would be like after this...")
        time.sleep(t)
        print("Type N to go to the next scene or E to end it right now (You will not see the afterword)")
        scene_choice = input()
        if scene_choice == "N":
            B_ED()
        elif scene_choice == "E":
            FIN()
        else:
            print("Error")
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return TAKE_ALL()








    def B_ED():
        print("After taking the treasure chest, you make your way back home")
        time.sleep(t)
        print("After that long and hard journey, you finally have something to get by with: those 1,000 coins")
        time.sleep(t)
        print("Finally,....")
        time.sleep(t2)
        #add time thing
        print("You pass away due to the shortage in coins.")
        time.sleep(t)
        print("Maybe those coins weren't enough to maintain yourself, but at least you died knowing you achieved something, right? ")
        time.sleep(t)
        print("Farewell, traveler.... You did an amazing job, but all stories come to an end.")
        time.sleep(t)
        print("END.")
















    def FIN():
        print("Thank you for playing our game. You may not know what happened after you got the treasure chest....")
        time.sleep(t2)
        print("But you will achieved something in this long and hard journey.")
        time.sleep(t)
        print("Congrats!!!")
        time.sleep(t)
        print("FIN/ END")
   
    ###








    print("Congrats! You have made it THIS far!!!!")
    time.sleep(t)
    print("For all your hard work, you stumble upon a treasure chest. Would you like to see the details?")
    chest_view = input()








    if chest_view == 'yes':
        print("Omg!! LOOK AT THIS!! ")
        time.sleep(t)
        print("This treasure chest contains many gold coins!!")
        time.sleep(t)
        print("This is worth 1000 gold coins! Can you believe it?! (...) ")
        time.sleep(t)
        print("ANYWAYS!! This chest is similar to what you have been looking for your whole journey!")
        time.sleep(t)
        print("Would you like to continue taking this with you and end your journey right here? Or would you rather donate it to charity!? Im sure many people could use this much gold coins. The choice is yours!")
        time.sleep(t)
        print("Type K to continue")
        CT_Game()








    elif chest_view == 'no':
        print("Are you sure you dont want to see the details?")
        time.sleep(t)
        print("This means that you choose to leave the treasure chest alone. Untouched.")
        time.sleep(t)
        print("(Dont worry, you will still continue on your journey.)")
        anothr_choice = input()
        if anothr_choice == 'yes':
            print('Alright, this means that you will leave this chest alone and continue on your journey.')
            time.sleep(t)
            print('Type J to continue')
            Continue_Gmae()
        elif anothr_choice == 'no':
            print("Does this mean you want to view the contents of this chest?")
            choice_agn = input()
            if choice_agn == 'yes':
                print("Okay.")
                time.sleep(t)
                print("Omg!! LOOK AT THIS!! ")
                time.sleep(t)
                print("This treasure chest contains many gold coins!!")
                time.sleep(t)
                print("This is worth 1000 gold coins! Can you believe it?! (...) ")
                time.sleep(t2)
                print("ANYWAYS!! This chest is similar to what you have been looking for your whole journey!")
                time.sleep(t)
                print("Would you like to continue take this with you and end your journey right here? Or would you rather donate it to charity!? Im sure many people could use this much gold coins. The choice is yours!")
                time.sleep(t)
                print("Type K to continue")
                CT_Game()
            if choice_agn == 'no':
                print('.....')
                time.sleep(t2)
                print('ok whatever...')
                time.sleep(t)
                print('Type J to continue')
                Continue_Gmae()
           








            else:
                print('error')
                x = True
                while x == True:
                    q = input("Would you like to continue? Y/N: ")
                    if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                        x = False
                        return DAY_20()
        else:
            print('error')
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return DAY_20()








    else:
        print('Error.')
        x = True
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                x = False
                return DAY_20()
















    def CT_Game():
        ulitmate_choice = input()
        if ulitmate_choice == 1:
            print('')
            print("Do you want to take this treasure chest with you? Or would you like to donate it to charity?")
            time.sleep(t)
            print("T for Treasure Chest annd C to donate to charity.")
            supr_chiice = input()
            if supr_chiice == 'T':
                print('You chose to open the treasure chest')
                TAKE_ALL()
            elif supr_chiice == 'C':
                CHARITY_W ()
                print('You have chose to donate to charity')
            else:
                print('Error')
                x = True
                while x == True:
                    q = input("Would you like to continue? Y/N: ")
                    if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                        x = False
                        return CT_Game()
        else:
            print('Error')
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return CT_Game()
       
























    def Continue_Gmae():
        anther_ultimte_chpice = input()
        if anther_ultimte_chpice == 2:
            print('')
            print("Are you going to continue on your journey? You will abandon the chest.")
            mega_choice = input()
            if mega_choice == 'yes':
                print("Alright. You proceed on your journey. Good luck on your travels!!")
                LAST_DAY_YAYY()
            elif mega_choice == 'no':
                print("Too bad you're going anyways.")
            else:
                print('Error')
                x = True
                while x == True:
                    q = input("Would you like to continue? Y/N: ")
                    if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                        x = False
                        return Continue_Gmae()
        else:
            print('Error')
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return Continue_Gmae()
       
















    def CHARITY_W ():
        print("OMG SO U HAVE CHOSEN TO DONATE TO CHARITY???")
        time.sleep(t)
        print("That is so kind of you!! Lets see what your fate will be.... ")
        time.sleep(t2)
        #add slep thing
        print(" Because you have chosen to donate to charity, the king and queen were impressed by your generosity. ")
        time.sleep(t)
        print("As a result... they have chosen to give you 1000000 gold coins")
        time.sleep(t)
        print("CONGRATSS YOU HAVE ACHIEVED THE BEST ENDING IN THIS GAME!!")
        time.sleep(t)
        print("END")








    def TAKE_ALL():
        print("SO U HAVE CHOSEN TO TAKE THIS TREASURE FOR YOURSELF???")
        time.sleep(t)
        print("That is..... interesting ")
        time.sleep(t2)
        print("Lets see what fate has in store for you.....")
        time.sleep(t2)
        print("You end your journey after taking the treasure chest with you")
        time.sleep(t)
        print("You wonder what your life would be like after this...")
        time.sleep(t2)
        print("Type N to go to the next scene or E to end it right now (You will not see the afterword)")
        scene_choice = input()
        if scene_choice == "N":
            B_ED()
        elif scene_choice == "E":
            FIN
        else:
            print('Error')
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return TAKE_ALL()








    def B_ED():
        print("After taking the treasure chest, you make your way back home")
        time.sleep(t)
        print("After that long and hard journey, you finally have something to get by wih: those 1,000 coins")
        time.sleep(t)
        print("Finally,....")
        time.sleep(t2)
        #add time thing
        print("You pass away due to the shortage in coins.")
        time.sleep(t)
        print("Maybe those coins weren't enough to maintain yourself, but atleast you died knowing you achieved something, right? ")
        time.sleep(t)
        print("Farewell, traveller.... You did an amazing job, but all stories come to an end.")
        time.sleep(t)
        print("END.")
















    def FIN():
        print("Thank you for playing our game. You may not know what happened after you got the treasure chest....")
        time.sleep(t2)
        print("But you will achieved something in this long and hard journey.")
        time.sleep(t)
        print("Congrats!!!")
        time.sleep(t)
        print("FIN/ END")




















#Day25








def LAST_DAY_YAYY():
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
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return LAST_DAY_YAYY()
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
            x = True
            while x == True:
                q = input("Would you like to continue? Y/N: ")
                if (q=="Yes" or q=="Y" or q=="yes" or q=="y"):
                    x = False
                    return LAST_DAY_YAYY()
















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
            if (q=="Yes" or q=="Y" or q=="y" or q=="yes"):
                x = False
                return journey()




journey()
#YAYYYY GAME FINISHED OMG UGE   finished may 31 finalyy
















#NOTES
#import other files (classflies)



