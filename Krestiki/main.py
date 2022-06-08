def welcome():
    print('Добро пожаловать в игру "Крестики-нолики"')
    print('Формат ввода координат x y')
    print('Где x это строка, y это столбец')





def show():
    print(f"   | 0 | 1 | 2 |")
    print('-'*19)
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print('-'*19)


def ask():
    while True:
        cords = input("Введите координаты:").split()
        if len(cords) != 2:
            print("Введите две координаты")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите число")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y




def chekc_win():
    win_check = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
    ]
    for cord in win_check:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print("Выиграл Крестик")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл Нолик")
                return True
    return False



welcome()
field = [[" "] * 3 for _ in range(3)]
num = 0
while True:
    num +=1

    show()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = ask()


    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if chekc_win():
        break

    if num == 9:
        print("Ничья")
        break
