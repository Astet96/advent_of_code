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
            cur_poz = TURN_FN[move[0]](cur_poz, int(move[1:]))
            if cur_poz == TARGET:
                match_cntr += 1
    print(match_cntr)

if __name__ == "__main__":
    get_pass()
