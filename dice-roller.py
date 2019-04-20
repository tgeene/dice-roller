import re
import random

print("\nDICE ROLLER")
print("-----")
print("Available commands: [dice equation]|reroll|exit")

user_input = ''
last_roll = ''

while user_input != 'exit':
    output = 0
    processed = 0
    
    if user_input == 'reroll':
        if last_roll:
            user_input = last_roll
        else:
            user_input = ''
            print('nothing to reroll')
    
    if user_input:
        last_roll = user_input
        
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
                    section_val = section_val + random.randrange(1, int(parts[1]))
            else:
                section_val = int(parts[0])
            
            if evaluation == '+':
                output = output + section_val
            else:
                output = output - section_val
            
        print(output)
    
    user_input = input('\nDice to roll: ')
