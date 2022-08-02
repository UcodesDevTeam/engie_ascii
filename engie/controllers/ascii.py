from typing import Tuple

import pandas
from pydantic import BaseModel, constr


class CharList(BaseModel):
    """
    Input schema for multiplying ASCII characters.
    """

    __root__: list[constr(min_length=1, max_length=1)]


def multiply_formula(char: int, multiply_by: float, ranges: list[Tuple[int, int]]):
    """
    Formula for multiplying characters if between ranges.

    :param char: Target character.
    :param multiply_by: Multiply by.
    :param ranges: Multiply by only if between these ranges.
    :return: Multiplied character or 0.
    """
    for r in ranges:
        if r[0] <= char <= r[1]:
            return char * multiply_by

    return 0


def multiply(chars: CharList) -> list[int]:
    """
    Multiplies the decimal representation of each character in the list by 10 given that
    said character is between a and h, A and H.

    :param chars: A list of ASCII characters.
    :return: A list of integers.
    """
    series = pandas.Series([ord(str(char)) for char in chars])
    series = series.apply(
        multiply_formula,
        multiply_by=10,
        ranges=[(ord("a"), ord("g")), (ord("A"), ord("G"))],
    )

    return series.tolist()
