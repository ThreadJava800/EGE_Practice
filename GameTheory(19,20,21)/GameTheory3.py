"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки
ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один или два
камня, или увеличить количество камней в куче в три раза.
Игра завершается в тот момент, когда количество камней в куче становится не менее 51.
Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, в
которой будет 51 или больше камней. Если при этом в куче оказалось не более 98 камней, то
победителем считается игрок, сделавший последний ход. В противном случае победителем
становится его противник.
В начальный момент в куче было S камней, 1 ≤ S ≤ 50.
Задание 19.
Найдите все значения S, при которых Ваня выигрывает первым ходом?
Задание 20.
Найдите наибольшее и наименьшее значения S, при которых Петя может выиграть своим
вторым ходом.
Задание 21.
Найдите значение S, при котором Ваня выигрывает своим первым или вторым ходом
"""


from functools import lru_cache


def move(h):
    a, b = h
    return (a+1, b), (a*3, b), (a+2, b)


@lru_cache(None)
def game(h):
    if sum(h) >= 51:
        if sum(h) <= 98:
            return 'W'
        else:
            return 'L'
    if any(game(m) == 'W' for m in move(h)):
        return 'P1'
    if all(game(m) == 'P1' or game(m) == 'L' for m in move(h)):
        return 'V1'
    if any(game(m) == 'V1' or game(m) == 'W' for m in move(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' or game(m) == 'L' for m in move(h)):
        return 'V12'


if __name__ == '__main__':
    for i in range(1, 51):
        if game((i, 0)) == 'V12':
            print(i)
