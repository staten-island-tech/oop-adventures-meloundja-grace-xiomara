#Day 20 (yayyy....  :| )






print("Congrats! You have made it THIS far!!!!")
print("For all your hard work, you stumble upon a treasure chest. Would you like to see the details?")
chest_view = input()

if chest_view == 'yes':
    print("Omg!! LOOK AT THIS!! ")
    print("This treasure chest contains many gold coins!!")
    print("This is worth 1000 gold coins! Can you believe it (...) ")
    print("ANYWAYS!! This chest is similar to what you have been looking for your whole journey!")
    print("Would you like to continue take this with you and end your journey right here? Or would you rather donate it to charity!? Im sure many people could use this much gold coins. The choice is yours!")
    print("Type anything to continue")
    ulitmate_choice = ()

elif chest_view == 'no':
    print("Are you sure you dont want to see the details?")
    print("This means that you choose to leave the treasure chest alone. Untouched.")
    print("(Dont worry, you will still continue on your journey.)")
    anothr_choice = input()
    if anothr_choice == 'yes':
        print('Alright, this means that you will leave this chest alone and continue on your journey.')
        print('Type anything to continue')
        anther_ultimte_chpice = ()
    elif anothr_choice == 'no': 
        print("Does this mean you want to view the contents of this chest?")
        choice_agn = input()
        if choice_agn == 'yes':
            print("Okay.")
            