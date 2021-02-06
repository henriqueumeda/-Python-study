s = input('Digite uma frase: ')
#s = 'azcbobobegghakl'
count = 0
for letter in s:
    if letter in 'aeiou':
        count += 1
print('Number of vowels: {}'.format(count))
