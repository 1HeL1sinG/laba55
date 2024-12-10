import random
import functools


def moves(x):
    return (x - 1, "1"), (x - 2, "2"), (x - 3, "3")


@functools.lru_cache(None)
def game(x):
    for m in moves(x):
        if m[0] == 1:
            return "WIN1", m[1]
    if all(game(m[0])[0] == 'WIN1' for m in moves(x)):
        return 'LOSS1', "1"
    for m in moves(x):
        if game(m[0])[0] == 'LOSS1':
            return 'WIN2', game(m[0])[1]
    else:
        return " "
    # if any(game(m[0]) == 'LOSS1' for m in moves(x)):
    #     return 'WIN2'


def main():
    n = random.randint(4, 30)
    print(f"Куча состоит из {n} камней")
    first_player = None
    if random.randint(0, 1):
        first_player = "pc"
        print("Первым ходит компьютер")
    else:
        first_player = "p"
        print("Первым ходит игрок")

    if first_player == "pc":
        while 1:
            print("Камней в куче =", n)
            turn = game(n)
            if turn == " ":
                turn = random.randint(1, 3)
                print(f"Компьютер вычел {turn} из {n}")
                n -= turn
            else:
                turn = int(turn[1])
                print(f"Компьютер вычел {turn} из {n}")
                n -= turn
            if n == 1:
                print("Камней в куче =", n)
                print("Вы проиграли )")
                break

            print("Камней в куче =", n)
            while 1:
                try:
                    turn = int(input("Сделайте ход(1, 2, 3) "))
                except ValueError:
                    print("Неверный ход")
                else:
                    if not (0 < turn < 4):
                        print("Неверный ход")
                        continue
                    break
            print(f"Вы отняли {turn} из {n}")
            n -= turn
            if n == 1:
                print("Камней в куче =", n)
                print("Компухтер проиграл ((")
                break

    #  Ходы если игрок первый
    else:
        while 1:
            print("Камней в куче =", n)
            while 1:
                try:
                    turn = int(input("Сделайте ход(1, 2, 3) "))
                except ValueError:
                    print("Неверный ход")
                else:
                    if not (0 < turn < 4):
                        print("Неверный ход")
                        continue
                    break
            print(f"Вы отняли {turn} из {n}")
            n -= turn
            if n == 1:
                print("Камней в куче =", n)
                print("Компухтер проиграл ((")
                break

            print("Камней в куче =", n)
            turn = game(n)
            if turn == " ":
                turn = random.randint(1, 3)
                print(f"Компьютер вычел {turn} из {n}")
                n -= turn
            else:
                turn = int(turn[1])
                print(f"Компьютер вычел {turn} из {n}")
                n -= turn
            if n == 1:
                print("Камней в куче =", n)
                print("Вы проиграли )")
                break


if __name__ == '__main__':
    main()
