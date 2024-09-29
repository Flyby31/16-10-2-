print("Перевод из двоичной системы в обычную")
choice_kunser = input('Будем переводить или расшифровывать (y/n)? ')
funki_kunki = input('Введите систему исчисления (2/16/10): ')

def funki(num):
    try:
        decimal_num = int(num, 2)
        return decimal_num
    except ValueError:
        return 'Ошибка: указано неверный формат двоичного числа'

def kunki(num):
    try:
        six_num = int(num, 16)
        return six_num
    except ValueError:
        return 'Ошибка: неверно введено число для перевода в 16-ричное число'

def tenki(num, target_base):
    try:
        ten_num = int(num, 10)  # Перевод в десятичную систему
        if target_base == '2':
            return bin(ten_num)[2:]  # Перевод в двоичную систему
        elif target_base == '16':
            return hex(ten_num)[2:]  # Перевод в шестнадцатеричную систему
        return ten_num  # Возврат числа в десятичной системе
    except ValueError:
        return 'Ошибка: неверно введено число для перевода в 10 число'

def choice_user(funki_kunki, num):
    if funki_kunki == '2':
        return funki(num)
    elif funki_kunki == '16':
        return kunki(num)
    elif funki_kunki == '10':
        return tenki(num, None)

num = input("Введите число: ")
if choice_kunser == 'y':  # Перевод
    result = choice_user(funki_kunki, num)
elif choice_kunser == 'n':  # Расшифровка
    result = tenki(num, funki_kunki)

print(result)
