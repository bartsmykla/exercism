"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter
from typing import List, Callable, Set, NewType

Dice = NewType("Dice", List[int])
ScoreCalculator = NewType("ScoreCalculator", Callable[[List[int]], int])


# Calculator function generators


def gen_occurences_calculator(expected: int) -> ScoreCalculator:
    return lambda dice: dice.count(expected) * expected


def gen_straight_calculator(expected_straight: Set[int]) -> ScoreCalculator:
    return lambda dice: 30 if set(dice) == expected_straight else 0


# Calculator functions


def yacht_calculator(dice: Dice) -> int:
    return 50 if len(set(dice)) == 1 else 0


def full_house_calculator(dice: Dice) -> int:
    return sum(dice) if {dice.count(n) for n in set(dice)} == {2, 3} else 0


def found_of_a_kind_calculator(dice: Dice) -> int:
    most_common = Counter(dice).most_common()

    return most_common[0][0] * 4 if most_common[0][1] >= 4 else 0


YACHT = yacht_calculator
ONES = gen_occurences_calculator(1)
TWOS = gen_occurences_calculator(2)
THREES = gen_occurences_calculator(3)
FOURS = gen_occurences_calculator(4)
FIVES = gen_occurences_calculator(5)
SIXES = gen_occurences_calculator(6)
FULL_HOUSE = full_house_calculator
FOUR_OF_A_KIND = found_of_a_kind_calculator
LITTLE_STRAIGHT = gen_straight_calculator({1, 2, 3, 4, 5})
BIG_STRAIGHT = gen_straight_calculator({2, 3, 4, 5, 6})
CHOICE = sum


def score(dice: Dice, score_calculator: ScoreCalculator) -> int:
    return score_calculator(dice)
