next_option = input()

if next_option == 'meat' or 'yes2':
    print('This is day 5 and it is time to make a new decision. Do you want to eat the meat you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
    choice = input()
    if choice == 'yes':
        print('ok, you may continue on your adventure')
    elif choice == 'no':
        print('You have straved to death and died. YOUR JOURNEY ENDS')


elif next_option == 'potion' or 'yes1':
    print('This is day 5 and it is time to make a new decision. Do you want to use the potion you bought? If you do not eat now then you will be eliminated. type yes to eat. Type no to die')
    choice = input()
    if choice == 'yes':
        print('Oops, seems like the potion you bought is poisoned so you just died ')
    elif choice == 'no':
        print('You have straved to death and died. YOUR JOURNEY ENDS')