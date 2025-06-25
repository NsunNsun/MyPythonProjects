import random

word_list = [
    "машина", "книга", "телефон", "компьютер", "программа",
    "учитель", "студент", "погода", "окно", "стол", "море", 
    "река", "город", "дерево", "собака", "кот", "музыка",
    "поезд", "самолёт", "игра", "яблоко", "апельсин","картина",
    "театр", "фильм",
]

charm_list = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def foolproofing(text, guessed_letters, guessed_words):
    if len(text) == 1 and text.upper() not in charm_list:
        print('Это не буква русского алфавита! Введите букву из алфавита: ')
        return True
    
    if text in guessed_letters:
        print('Ты уже отгадал эту букву! Введите другую: ')
        return True

    elif text in guessed_words:
        print('Ты уже пробовал это слово! Введите другое слово: ')
        return True
    
    else:
        return False

def play(word):
    print('Давайте играть в угадайку слов!')
    tries = 6                          # количество попыток
    print(display_hangman(tries))
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    print(word_completion)
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    guessed = False                    # сигнальная метка

    guessed_word_list = list(word)
    word_completion_list = list(word_completion)
    
    while guessed == False and tries > 0:
        repeat = 0
        guess = input('\nВведите ваше слово или букву: ').upper()

        while foolproofing(guess, guessed_letters, guessed_words):
            repeat += 1
            if repeat >= 3:
                print('Вы проиграли!')
                print(display_hangman(0))
                return
            guess = input('\nВведите ваше слово или букву: ').upper()
       
        if guess == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            print(display_hangman(tries))
            print(word)
            guessed = True
            answer = input('Хотите сыграть еще раз?').lower()
            if answer in ['д', 'да', 'конечно']:
                play(get_word())
                return
            else:
                print('Спасибо за игру!')
                return

        elif len(guess) == 1:
            if guess in word:
                for i in range(len(guessed_word_list)):
                    if guessed_word_list[i] == guess:
                        word_completion_list[i] = guess                                                                                           
                    else:
                        continue
                print('Такая буква есть.')
                tries -= 1

            else:
                print('Такой буквы к сожаленю нет. Попробуйте ещё.')
                tries -= 1

            if guess not in guessed_letters:
                guessed_letters.append(guess)

        else:
            count_charm_word = 0
            for j in guess:
                if j in guessed_word_list:
                    for h in range(len(guessed_word_list)):
                        if guessed_word_list[h] == j:
                            word_completion_list[h] = j
                    if j not in guessed_letters:
                        guessed_letters.append(j)
                    count_charm_word += 1

            if guess not in guessed_words:
                guessed_words.append(guess)

            if count_charm_word == 0:
                print('Таких букв к сожаленю нет. Попробуйте ещё.')
                tries -= 1
            elif count_charm_word == 1:
                print('Вы отгадали одну букву! Попробуйте ещё.')
                tries -= 1
            else:
                print('Поздравляю!! Вы отгадали несколько букв. Попробуйте ещё.')
                tries -= 1

            print(display_hangman(tries))
            print(''.join(word_completion_list))

        
        if "_" not in word_completion_list:
            guessed = True
            print('Поздравляем, вы угадали слово! Вы победили!')
            answer = input('Хотите сыграть еще раз?').lower()
            if answer in ['д', 'да', 'конечно']:
                play(get_word())
                return
            else:
                print('Спасибо за игру!')
                return

    print('Боюсь ваши попытки закончились. Спасибо за игру.')
    print(display_hangman(tries))
    print(word)

play(get_word())