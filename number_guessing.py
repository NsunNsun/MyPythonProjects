import random

print('Добро пожаловать в числовую угадайку')

def is_valid_number(text):
    return text.isdigit() and 1 <= int(text) <= 100

def is_valid_text(text):
    return text.lower() == "д" or text.lower() == "н"

def game():
    guest_number = input('В каком диапазоне ты хочешь отгадать чилсло?')
    random_number = random.randint(1, int(guest_number))
    count = 0

    while True:
        user_text = input('Введите ваше число: ')

        if is_valid_number(user_text):
            user_text = int(user_text)
            count += 1

            if user_text < random_number:
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif user_text > random_number:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print("Вы угадали, поздравляем!", "Количество попыток:", count)
                repeat_game()
                break

        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

def repeat_game():
    count_repeat = 0

    while count_repeat < 3:
        print("Хотите сыграть еще раз?", "д = да и н = нет")
        user_answer = input()

        if is_valid_text(user_answer):
            if user_answer == "д":
                game()
            else:
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                break
        else:
            print("Введите д или н")
            count_repeat += 1

    if count_repeat >= 3:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
    

game()