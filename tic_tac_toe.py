playing_field = [[' '] * 3 for _ in range(3)]
c = 1
cord = {k: None for k in range(1, 10)}
for i in range(3):
    for j in range(3):
        cord[c] = (i, j)
        c += 1


def show_field():
    print('          ' + '-' * 13)
    for row in playing_field:
        print(f"          | {' | '.join(row)} |")
        print('          ' + '-' * 13)


def end_text(st):
    print('    ' + "*" * 26)
    print(f'    ***** | {st} | *****')
    print('    ' + '*' * 26)


def correct_pos():
    while True:
        moved = input("  Введите число: ")
        if not moved.isdigit():
            print("Ошибка ввода, введите целое число")
            continue
        if not (1 <= int(moved) <= 9):
            print("Число не входит в диапозон [1:9]")
            continue
        if playing_field[cord[(int(moved))][0]][cord[(int(moved))][1]] != " ":
            print("Эта ячейка уже занята")
            continue
        return int(moved)


def winner(sym, fl=True):
    win_cord = [
        (cord[1], cord[2], cord[3]), (cord[4], cord[5], cord[6]), (cord[7], cord[8], cord[9]),
        (cord[1], cord[4], cord[7]), (cord[2], cord[5], cord[8]), (cord[3], cord[6], cord[9]),
        (cord[1], cord[5], cord[9]), (cord[3], cord[5], cord[7])
    ]

    for x, y, z in win_cord:
        if playing_field[x[0]][x[1]] == playing_field[y[0]][y[1]] == playing_field[z[0]][z[1]] == sym:
            fl = False
            break
    return fl


def pict_field(sym):
    show_field()
    print(f"  --------- ХОДИТ |{sym}| ---------")
    n = correct_pos()
    x, y = cord[n]
    playing_field[x][y] = sym


count_move = 0
flag = True
while flag and count_move < 9:
    for s in ("X", "0"):
        pict_field(s)
        count_move += 1
        flag = winner(s)
        if not flag:
            end_text(f'ПОБЕДИЛ  {s}')
            show_field()
            break
        if count_move == 9:
            end_text(' НИЧЬЯ!!! ')
            show_field()
            break

else:
    end_text('КОНЕЦ ИГРЫ')
