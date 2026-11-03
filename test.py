door_unlocked = False
card_valid = 'Red'
pin_correct = 1234


while door_unlocked == False:
	try:
		user_card = input('Swipe your card! (Red, Green, Blue):  ')
		break
	except ValueError:
		print('Invalid Access card')

if card_valid == user_card:
	print('Valid Access card')
	pin_guess = int(input('Enter your PIN! (4 digits):  '))

	if pin_guess == pin_correct:
		print('Access Granted!')
		if pin_guess == pin_correct and card_valid == user_card:
			door_unlocked = True
			print('Door Unlocked!')

	else:
			print('Invalid PIN')