import random
import time

word_list = [
    "машина", "книга", "телефон", "компьютер", "программа",
    "учитель", "студент", "погода", "окно", "стол",
    "море", "река", "город", "дерево", "собака",
    "кот", "музыка", "поезд", "самолёт", "игра",
    "яблоко", "апельсин", "картина", "театр", "фильм",
]

charm_list = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
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
        print('Это не буква русского алфавита! Введите букву из алфавита.')
        return True

    if text in guessed_letters:
        print('Ты уже отгадал эту букву! Введите другую.')
        return True

    if text in guessed_words:
        print('Ты уже пробовал это слово! Введите другое слово.')
        return True

    return False

def show_word_state(word_completion_list):
    print('Текущее состояние слова: ' + ''.join(word_completion_list))

def play(word):
    print('Давайте играть в угадайку слов!')
    tries = 6
    print(display_hangman(tries))
    
    word_completion_list = ['_' for _ in word]
    show_word_state(word_completion_list)

    guessed_letters = []
    guessed_words = []
    guessed = False

    while not guessed and tries > 0:
        guess = input('\nВведите ваше слово или букву: ').upper()

        repeat = 0
        while foolproofing(guess, guessed_letters, guessed_words):
            repeat += 1
            if repeat >= 3:
                print('Слишком много неправильных попыток ввода. К сожалению, вы проиграли.')
                print(display_hangman(0))
                return
            guess = input('\nПопробуйте ввести снова слово или букву: ').upper()

        if guess == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            time.sleep(1.5)
            guessed = True
            break

        elif len(guess) == 1:
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion_list[i] = guess
                print('Отлично! Такая буква есть.')
            else:
                print('Увы, такой буквы в слове нет. Попробуйте ещё раз — у вас всё получится!')
                tries -= 1

            if guess not in guessed_letters:
                guessed_letters.append(guess)

        else:
            count_charm_word = 0
            for letter in guess:
                if letter in word:
                    for i in range(len(word)):
                        if word[i] == letter:
                            word_completion_list[i] = letter
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                    count_charm_word += 1

            if guess not in guessed_words:
                guessed_words.append(guess)

            if count_charm_word == 0:
                print('К сожалению, таких букв в слове нет. Не сдавайтесь, попробуйте ещё!')
                tries -= 1
            elif count_charm_word == 1:
                print('Вы угадали одну букву, здорово! Давайте продолжим.')
                tries -= 1
            else:
                print('Великолепно! Вы угадали несколько букв. Продолжаем! :)')
                tries -= 1

        print(display_hangman(tries))
        show_word_state(word_completion_list)
        time.sleep(1)  # пауза перед следующим ходом

        if '_' not in word_completion_list:
            print('Поздравляем, вы угадали слово! Вы победили!')
            time.sleep(1.5)
            guessed = True

    if not guessed:
        print('Боюсь, ваши попытки закончились. Спасибо за игру.')
        print(f'Загаданное слово было: {word}')
        print(display_hangman(0))

def main():
    while True:
        word = get_word()
        play(word)
        answer = input('\nХотите сыграть еще раз? (да/нет): ').lower()
        if answer not in ['д', 'да', 'конечно']:
            print('Спасибо за игру! До новых встреч!')
            break

main()
