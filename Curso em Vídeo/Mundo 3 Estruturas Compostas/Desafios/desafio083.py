character_list = []
expression = input('Input a math expression: ')
for character in expression:
    if character == '(':
        character_list.append(character)
    elif character == ')':
        if len(character_list) > 0:
            character_list.pop()
        else:
            character_list.append(character)
            break

if len(character_list) == 0:
    print('Your expression is valid.')
else:
    print('Your expression is invalid.')
