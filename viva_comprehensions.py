from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> list:
    """
      Generate a list
      
    :param start:
    :param stop:
    :param parity:
    :return:
    """
    if parity == Parity.EVEN:
        return [val for val in range(start, stop) if val % 2 == 0]
    else:
        return [val for val in range(start, stop) if val % 2 != 0]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
     Generate a dictionary

    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    return {i: strategy(i) for i in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    Generate a set

    :param val_in:
    :return:
    """

    return set(char for char in val_in.swapcase() if char.isupper())
