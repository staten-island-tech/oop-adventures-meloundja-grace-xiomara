<<<<<<< Updated upstream
option = input('what would you like to bring with you on your travels? Meat is 90 gold coins and potion is 50 gold coins. They will both last 25 days of your adventure(meat/potion)')
=======
option = input('what would you like to bring with you on your travels? Meat is 90 gold coins and potion is 50 gold coins. They will both last 50 days of your adventure(meat/potion)')
>>>>>>> Stashed changes
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


<<<<<<< Updated upstream
=======






>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    print('This is day 5 and it is time to make a new decision. Do you want to eat the meat you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
=======
    print('This is day 5 and it is time to make a new decision. Do you want to eat the food you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
>>>>>>> Stashed changes
    choice = input()
    if choice == 'yes':
        print('ok, you may continue on your adventure')
    elif choice == 'no':
        print('You have starved to death and died. YOUR JOURNEY ENDS')


<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
elif next_option == 'potion' or 'yes1':
    print('This is day 5 and it is time to make a new decision. Do you want to use the potion you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
    choice = input()
    if choice == 'yes':
        print('Oops, seems like the potion you bought is poisoned so you just died ')
    elif choice == 'no':
        print('You have starved to death and died. YOUR JOURNEY ENDS')
<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
