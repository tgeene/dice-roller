import re
import random

print("\nDICE ROLLER")
print("-----")
print("Available commands: [equation|reroll|exit]")
print("Equation Format: #d#[+#d#|#[...]]")

user_input = ''
last_roll = ''

while user_input != 'exit':
	if user_input == 'reroll':
		if last_roll:
			user_input = last_roll
		else:
			user_input = ''
			print('nothing to reroll')
	
	if re.search(r'(\d+d\d+)((\+((\d+d\d+)|\d+))*)?', user_input):
		last_roll = user_input
		
		output = 0
		processed = 0
		
		sections = re.split("\+|\-", user_input)
		for section in sections:
			if processed:
				evaluation = user_input[processed]
				processed = processed + 1
			else:
				evaluation = '+'
			
			processed = processed + len(section)
			parts = re.split("d", section)
			
			section_val = 0
			if len(parts) == 2:
				for n in range(0, int(parts[0])):
					dice_roll = random.randrange(1, int(parts[1]))
					print(f"d{parts[1]}: {dice_roll}")
					section_val = section_val + dice_roll
			else:
				section_val = int(parts[0])
			
			if evaluation == '+':
				output = output + section_val
			else:
				output = output - section_val
			
		print("--")
		print(f"Total: {output}")
	elif user_input != '':
		print("Invalid Command. Please Try Again.")
	
	user_input = input('\nDice to roll: ')
	user_input = user_input.replace(" ", "")
