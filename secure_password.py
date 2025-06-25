import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
ambiguous = "il1Lo0O"


chars = ""

quantity = int(input("Сколько паролей нужно сгенерировать? "))
length_password = int(input("\nКакая длина одного пароля? "))

need_digits = input("\nВключать ли цифры? 0123456789 ")
need_lowercase_letters = input(
    "\nВключать ли строчные буквы? abcdefghijklmnopqrstuvwxyz "
)
need_uppercase_letters = input(
    "\nВключать ли прописные буквы? ABCDEFGHIJKLMNOPQRSTUVWXYZ "
)
need_punctuation = input("\nВключать ли символы? !#$%&*+-=?@^_ ")
need_exceptions = input("\nИсключать ли неоднозначные символы il1Lo0O ")


if need_digits == "да":
    chars += "".join(digits)
if need_lowercase_letters == "да":
    chars += "".join(lowercase_letters)
if need_uppercase_letters == "да":
    chars += "".join(uppercase_letters)
if need_punctuation == "да":
    chars += "".join(punctuation)

if need_exceptions == "да":
    for i in ambiguous:
        chars = chars.replace(i, "")

chars_list = list(chars)

def generate_password(length, chars):
    for _ in range(quantity):
        print()
        print(''.join(random.sample(chars, length)))

generate_password(length_password, chars_list)
