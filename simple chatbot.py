def take_input():
	ui = input('Hi, I am a mini chatbot\n')

	if ui.lower() == 'hi':
		print('Hello\n')
	elif ui.lower() == 'how are you':
		print('i am doing well,what about you\n')
	elif ui.lower() == 'how':
		print('what',"how",'\n')
	
		
	else:
			print('i dont know what is that\n')
			
	while True:
		ui = input('What should i do next for you\n')
		
		if ui.lower() == 'hi':
			print('Hello\n')
		elif ui.lower() == 'how are you':
			print('i am doing well,what about you\n')
		elif ui.lower() == 'hello':
			print('Hello')
		elif ui.lower() == 'how':
			print('what',"how",'\n')
		elif ui.lower() == 'fine':
			print('me too\n')
			
		else:
			print('i dont know what is that\n')

take_input()