import random
money: int = 500
rep = 0
def stock_exchange():
    global money
    a = random.randint(300, money)
    print("Текущая цена:", a)
    solution = input("Совершаем покупку?(Да/Нет)")
    result = random.randint(1, 2)
    if solution == "Нет":
        print("В следущий раз")
    elif solution == "Да":
        if result == 1:
            print("Ставка зашла, на ваш баланс зачисленно", a, "$")
            money += a
            print("Ваш баланс", money, "$")
        elif result == 2:
            print("Не повезло, приходи в следущий раз")

def show_menu():
    print("\nCимулятор крипто-биржи Меню:")
    print("1. Посмотреть свой баланс")
    print("2. Идти на биржу")
    print("3. Отдать все деньги на благотворительность")
    print("4. Посмотреть свою репутацию")

def Balance():
    print("Ваш баланс:", money, "$")

def blago():
    global money
    global rep
    money = 500
    rep += 1

def repp():
    if rep == 0:
        print("Всем все ровно на вас")
    if rep == 1:
        print("У вас хорошая репутация")
while True:
    show_menu()
    choice = input("Ваш выбор: ")

    if choice == "1":
        Balance()
    elif choice == "2":
        stock_exchange()
    elif choice == "3":
        blago()
    elif choice == "4":
        repp()
    else:
        print("Неправильный выбор. Повторите попытку.")