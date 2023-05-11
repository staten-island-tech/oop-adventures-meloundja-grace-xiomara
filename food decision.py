option = input('what would you like to bring with you on your travels?(meat/potion)')
if option == 'meat':
    print('cost is 90 gold coins')
    choice = input('do you still want to purchase this item?')
    if choice == 'yes':
        print('you have 10 coins left')
    elif choice == 'no':
        print('Okay so you want potion instead?')
        choice = input()
        if choice == 'yes':
            print('okay you hve 50 coins left and continued on your journey')
        elif choice == 'no':
            print('thank you for visiting but unforunately you will die due to stravation on your adventure')
        else:
            print('not a choice')




elif option == 'potion':
    print('cost is 50 gold coins')
    choice = input('do you still want to purchase this item?')
    if choice == 'yes':
        print('you have 50 coins left')
    elif choice == 'no':
            print('Okay')




else:
    print('not in stock')

if option == 'meat':
    print('This is day 5 and it is time to make a new decision. Do you want to eat the meat you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
    choice = input()
    if choice == 'yes':
        print('ok, you may continue on your adventure')
    elif choice == 'no':
        print('You have straved to death and died. YOUR JOURNEY ENDS')


elif option == 'potion':
    print('This is day 5 and it is time to make a new decision. Do you want to use the potion you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
    choice = input()
    if choice == 'yes':
        print('Oops, seems like the potion you bought is poisoned so you just died ')
    elif choice == 'no':
        print('You have straved to death and died. YOUR JOURNEY ENDS')
