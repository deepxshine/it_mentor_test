from typing import Tuple
from exceptions import InputError, OperationError


def read_input() -> Tuple[int, int, str]:
    data = input().split()
    if len(data) != 3:
        raise InputError
    a, opp, b = data
    try:
        a, b = int(a), int(b)
        return a, b, opp
    except Exception:
        raise InputError


def calculator(a: int, b: int, opperation: str) -> int:
    opperations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }
    if opperation not in opperations.keys():
        raise OperationError
    result = opperations[opperation](a, b)
    return result


def main() -> None:
    a, b, opperation = read_input()
    res = calculator(a, b, opperation)
    print(res)


if __name__ == '__main__':
    main()
