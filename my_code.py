number_dict = [
    {"0":[" "]}, {"1":[".", ",", "?", "!", ":"]}, {"2":["A", "B", "C"]}, 
    {"3":["D", "E", "F"]}, {"4":["G", "H", "I"]}, {"5":["J", "K", "L"]}, 
    {"6":["M", "N", "O"]}, {"7":["P", "Q", "R", "S"]}, {"8":["T", "U", "V"]}, 
    {"9":["W", "X", "Y", "Z"]}
]

text = list(input().upper())
number_list = []

for i in range(len(text)):
    for j in range(len(number_dict)):
        if text[i] in number_dict[j][str(j)]:
            number_list += list(number_dict[j].keys()) * (number_dict[j][str(j)].index(text[i]) + 1)
            break

print("".join(number_list))
