import os
from typing import Callable

CWD :str = os.path.dirname(os.path.realpath(__file__))
IN_FILE :str = os.sep.join([CWD, 'input'])

START : int = 50
TARGET : int = 0
MIN : int = 0
MAX : int = 99

TURN_FN : dict[str, Callable[[int, int], int]] = {
    'L': lambda poz, incr: (MAX + 1 + poz - incr)%(MAX+1),
    'R': lambda poz, incr: (poz + incr)%(MAX+1),
}

def get_pass() -> None:
    match_cntr = 0
    cur_poz = START
    with open(IN_FILE, 'r') as fl:
        for move in fl.readlines():
            direction, increment = move[0], int(move[1:])
            if direction not in TURN_FN.keys():
                raise ValueError(f"$direction can only be 'L' or 'R', got '{direction}' instead!")
            match_cntr += increment//(MAX+1)
            increment %= (MAX+1)

            match direction:  # pyright: ignore[reportMatchNotExhaustive]
                case 'L':
                    if cur_poz != MIN and cur_poz <= increment:
                        match_cntr += 1
                case 'R':
                    if cur_poz + increment > MAX:
                        match_cntr += 1

            cur_poz = TURN_FN[direction](cur_poz, increment)

    print(match_cntr)

if __name__ == "__main__":
    get_pass()
