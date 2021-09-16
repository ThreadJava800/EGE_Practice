from functools import lru_cache


def move(h):
    a, b = h
    return (a+1, b), (a*2, b)


@lru_cache(None)
def game(h):
    if sum(h) >= 33:
        return 'W'
    if any(game(m) == 'W' for m in move(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in move(h)):
        return 'V1'
    if any(game(m) == 'V1' for m in move(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in move(h)):
        return 'V12'


if __name__ == '__main__':
    for i in range(1, 51):
        if game((i, 0)) == 'V1':
            print(i)
