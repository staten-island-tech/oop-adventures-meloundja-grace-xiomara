#Day 20 (yayyy....  :| )


###
def CT_Game ():
    print('Type K to continue')
    ulitmate_choice = input()
    if ulitmate_choice == "K":
        print('')
        print("Do you want to take this treasure chest with you? Or would you like to donate it to charity?")
        print("T for Treasure Chest annd C to donate to charity.")
        supr_chiice = input()
        if supr_chiice == 'T':
            print('You chose to open the treasure chest')
        elif supr_chiice == 'C':
            print('You have chose to donate to charity')
        else:
            print('Error')
    else:
        print('Error')
        



def Continue_Gmae():
    print("type J to continue")
    anther_ultimte_chpice = input()
    if anther_ultimte_chpice == "J":
        print('')
        print("Are you going to continue on your journey? You will abandon the chest.")
        mega_choice = input()
        if mega_choice == 'yes':
            print("Alright. You proceed on your journey. Good luck on your travels!!")
        elif mega_choice == 'no':
            print("Too bad you're going anyways.")
        else:
            print('Error')
    else: 
        print('Error')
        
###

print("Congrats! You have made it THIS far!!!!")
print("For all your hard work, you stumble upon a treasure chest. Would you like to see the details?")
chest_view = input()

if chest_view == 'yes':
    print("Omg!! LOOK AT THIS!! ")
    print("This treasure chest contains many gold coins!!")
    print("This is worth 1000 gold coins! Can you believe it?! (...) ")
    print("ANYWAYS!! This chest is similar to what you have been looking for your whole journey!")
    print("Would you like to continue take this with you and end your journey right here? Or would you rather donate it to charity!? Im sure many people could use this much gold coins. The choice is yours!")
    print("Type K to continue")
    CT_Game()

elif chest_view == 'no':
    print("Are you sure you dont want to see the details?")
    print("This means that you choose to leave the treasure chest alone. Untouched.")
    print("(Dont worry, you will still continue on your journey.)")
    anothr_choice = input()
    if anothr_choice == 'yes':
        print('Alright, this means that you will leave this chest alone and continue on your journey.')
        print('Type J to continue')
        Continue_Gmae()
    elif anothr_choice == 'no': 
        print("Does this mean you want to view the contents of this chest?")
        choice_agn = input()
        if choice_agn == 'yes':
            print("Okay.")
            print("Omg!! LOOK AT THIS!! ")
            print("This treasure chest contains many gold coins!!")
            print("This is worth 1000 gold coins! Can you believe it?! (...) ")
            print("ANYWAYS!! This chest is similar to what you have been looking for your whole journey!")
            print("Would you like to continue take this with you and end your journey right here? Or would you rather donate it to charity!? Im sure many people could use this much gold coins. The choice is yours!")
            print("Type K to continue")
            CT_Game()
        if choice_agn == 'no':
            print('.....')
            print('ok whatever...')
            print('Type J to continue')
            Continue_Gmae()
            

        else:
            print('error')
    else:
        print('error')

else:
    print('Error.')


def CT_Game():
    ulitmate_choice = input()
    if ulitmate_choice == 1:
        print('')
        print("Do you want to take this treasure chest with you? Or would you like to donate it to charity?")
        print("T for Treasure Chest annd C to donate to charity.")
        supr_chiice = input()
        if supr_chiice == 'T':
            print('You chose to open the treasure chest')
        elif supr_chiice == 'C':
            print('You have chose to donate to charity')
        else:
            print('Error')
    else:
        print('Error')
        



def Continue_Gmae():
    anther_ultimte_chpice = input()
    if anther_ultimte_chpice == 2:
        print('')
        print("Are you going to continue on your journey? You will abandon the chest.")
        mega_choice = input()
        if mega_choice == 'yes':
            print("Alright. You proceed on your journey. Good luck on your travels!!")
        elif mega_choice == 'no':
            print("Too bad you're going anyways.")
        else:
            print('Error')
    else: 
        print('Error')
        


def CHARITY_W ():
    print("OMG SO U HAVE CHSOEN TO DONATE TO CHARITY???")
    print("That is so kind of you!! Lets see what your fate will be.... ")
    #add slep thing
    print(" Because you have chosen to donate to charity, the king and queen were impressed by your generosity. ")
    print("As a result... they have chosen to give you 1000000 gold coins")
    print("CONGRATSS YOU HAVE ACHIEVED THE BEST ENDING IN THIS GAME!!")
    print("END")

def TAKE_ALL(): 
    print("SO U HAVE CHOSE TO TAKE THIS TREASURE FOR YOURSELF???")
    print("That is..... interesting ")
