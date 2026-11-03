door_unlocked = False
card_valid = 'Red'
pin_correct = 1234


if door_unlocked == False:
	print('Swipe your card!')
	user_card = input('(Red, Green, Blue):  ')
	
        if card_valid == user_card:
	        print('Valid Access card')
	        print('Enter your PIN!')
	        pin_guess = int(input('(4 digits): '))

            if pin_guess == pin_correct:
		        print('Access Granted!')

	                if pin_guess == pin_correct and card_valid == user_card:
		                door_unlocked = True
                        print('Door Unlocked!')
            else:
                print('Invalid PIN')

        else:
            print('Invalid Access card')

else:
    print("Welcome in")