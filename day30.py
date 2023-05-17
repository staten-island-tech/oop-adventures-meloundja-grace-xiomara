last_choice = input('You just arrived at the kingdom of island 4, and here sits the treasure chest that you have long awaited. Would you like to open the chest or go home? (open chest/ go home) ')

if last_choice == 'go home':
    print('Ok guess all that work was for nothing. Your journey....')
    print("ENDS!!!!")
    print('Sorry that you suck at this game, but thanks for playing anyway ;) BYE!')

    
elif last_choice == 'open chest':
    print('There is the long awaited treasure you have longed for that will make you rich... HUH all you see is a few cabbages and a note inside. Would you like to read the note? (sure/nah)')

else:
        print('not a choice. take this game seriously and put in the right choice')
read_letter = input()

if read_letter == 'sure':
        print('Unfortunately you have failed the test. Due to your greediness, you even ditched the 1000 gold coins. Instead of donating the money to chairty you failed. To make you feel better, here are some cabbages as a gift for your long journey.')
        print('Thanks for playing this awesome rage quitting game. Hope you have a good day. Goodbye')

elif read_letter == 'nah':
        print('well guess you go home with your cabbage without knowing why there is no treasure in it and strave to death because you are a brokie.')
        print('Thanks for playing. BYE BYE!!!')

else:
        print('not a choice. take this game seriously and put in the right choice by reading the instructions')


