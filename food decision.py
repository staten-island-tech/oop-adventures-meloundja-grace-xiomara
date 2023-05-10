option = input('what would you like to bring with yu on your travels?(meat/potion)')
if option == 'meat':
    print('cost is 90 gold coins')
    choice = input('do you still want to purchase this item?')
    if choice == 'yes':
        print('you have 10 coins left')
    elif choice == 'no':
            print('Okay')


elif option == 'potion':
    print('cost is 50 gold coins')
    choice = input('do you still want to purchase this item?')
    if choice == 'yes':
        print('you have 50 coins left')
    elif choice == 'no':
            print('Okay')


else:
    print('not in stock')

