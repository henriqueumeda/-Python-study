s = input('Write something: ')
#s = 'azcbobobegghakl'
count = 0
for position in range(0, len(s)-2):
    word = s[position] + s[position+1] + s[position+2]
    if word == 'bob':
        count += 1
print('Number of times bob occurs is: {}'.format(count))
