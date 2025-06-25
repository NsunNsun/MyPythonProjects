

lowercase_letters_en = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters_en = lowercase_letters_en.upper()
lowercase_letters_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
uppercase_letters_ru = lowercase_letters_ru.upper()

purpose_enquiry = input("Что вы хотите сделать? Зашифровать - з или Дешифровать - д?\n")
language = input("какой язык будем использовать? Русский - р или Английский - а?\n")
shift_step = int(input("Какой шаг сдвига? Введите число: \n"))

def text_operation():
    if purpose_enquiry.lower().strip() == 'з' or purpose_enquiry.lower().strip() == 'Зашифровать':
        user_text = input("Какую фразу вы хотите Зашифровать\n")
    else:
        user_text = input("Какую фразу вы хотите Дешифровать\n")

    return user_text

user_text = text_operation()

def encryption_ru(text):
    encryption_user_text = []
    for i in range(len(text)):
        position = lowercase_letters_ru.find(text[i].lower())
        if position < 0:
            encryption_user_text.append(text[i])
            continue
        new_position = (position + shift_step) % len(lowercase_letters_ru)

        if text[i] in uppercase_letters_ru:
            encryption_user_text.append(uppercase_letters_ru[new_position])
        elif text[i] in lowercase_letters_ru:
            encryption_user_text.append(lowercase_letters_ru[new_position])

    print(''.join(encryption_user_text))

def decryption_ru(text):
    decryption_user_text = []
    for i in range(len(text)):
        position = lowercase_letters_ru.find(text[i].lower())
        if position < 0:
            decryption_user_text.append(text[i])
            continue
        new_position = (position - shift_step) % len(lowercase_letters_ru)

        if text[i] in uppercase_letters_ru:
            decryption_user_text.append(uppercase_letters_ru[new_position])
        elif text[i] in lowercase_letters_ru:
            decryption_user_text.append(lowercase_letters_ru[new_position])
        
    print(''.join(decryption_user_text))

def encryption_en(text):
    encryption_user_text = []
    for i in range(len(text)):
        position = lowercase_letters_en.find(text[i].lower())
        if position < 0:
            encryption_user_text.append(text[i])
            continue
        new_position = (position + shift_step) % len(lowercase_letters_en)

        if text[i] in uppercase_letters_en:
            encryption_user_text.append(uppercase_letters_en[new_position])
        elif text[i] in lowercase_letters_en:
            encryption_user_text.append(lowercase_letters_en[new_position])

    print(''.join(encryption_user_text))

def decryption_en(text):
    decryption_user_text = []
    for i in range(len(text)):
        position = lowercase_letters_en.find(text[i].lower())
        if position < 0:
            decryption_user_text.append(text[i])
            continue
        new_position = (position - shift_step + j) % len(lowercase_letters_en)

        if text[i] in uppercase_letters_en:
            decryption_user_text.append(uppercase_letters_en[new_position])
        elif text[i] in lowercase_letters_en:
            decryption_user_text.append(lowercase_letters_en[new_position])

    print(''.join(decryption_user_text))

if purpose_enquiry.lower().strip() == 'з' or purpose_enquiry.lower().strip() == 'Зашифровать':
    if language.lower().strip() == 'р' or language.lower().strip() == 'Русский':
        encryption_ru(user_text)
    else:
        encryption_en(user_text)
else:
    if language.lower().strip() == 'р' or language.lower().strip() == 'Русский':
        decryption_ru(user_text)
    else:
        decryption_en(user_text)
