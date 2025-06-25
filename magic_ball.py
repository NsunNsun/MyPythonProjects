import random

answers = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется — да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят — да",
    "Да",
    "Пока не ясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ — нет",
    "По моим данным — нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
guest_name = input("Как тебя зовут? ")
print("Привет", guest_name)


def is_valid_text(text):
    return text.lower() in ('д', 'н')


def game():
    while True:
        guest_question = input("\nКакой у тебя есть вопрос? ")
        print("🔮", random.choice(answers))
        repeat_game()
        break


def repeat_game():

    count_repeat = 0

    while count_repeat < 3:
        print()
        print("Ты хочешь задать еще один вопрос? " "д = да и н = нет")
        user_answer = input()

        if is_valid_text(user_answer):
            if user_answer == "д":
                game()
            else:
                print("Возвращайся, если возникнут вопросы!")
                break
        else:
            print("Введите д или н")
            count_repeat += 1

    if count_repeat >= 3:
        print("Возвращайся, если возникнут вопросы!")


game()