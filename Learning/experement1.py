word = "*!*!*?"
word_list = list(word)
dict_length = 3

dict_book = {3: 'а', 2: 'н', 1: 'с'}

#re_puzzle_dict = {3: '*', 2: '!', 1: '?'}
puzzle_dict = {'*': 3, '!': 2, '?': 1}

clear_word = ""

for x in word_list:
    clear_word += dict_book[puzzle_dict[x]]
    




print(clear_word)

