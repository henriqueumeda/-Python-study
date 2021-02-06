s = input('Write something: ')
#s = 'azcbobobegghakl'
#s = 'abcbcd'
character_list = []
for letter in s:
    character_list += letter
ordered_list = sorted(character_list)
counter = 0
for letter in s:
    counter += 1
    if counter == 1:
        word = letter
        longest_word = letter
    else:
        letter_index = ordered_list.index(letter)
        word_last_character_index = ordered_list.index(word[-1])
        if letter_index >= word_last_character_index:
            word += letter
            if len(word) > len(longest_word):
                longest_word = word
        else:
            word = letter
print(longest_word)