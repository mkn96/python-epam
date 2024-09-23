from __future__ import annotations
from typing import Type


class Currency:
    def __init__(self, value):
        self.value = value

    def to_currency(self, cls):
        return cls(self.value / self.course(cls))

    def __add__(self, other):
        return self.__class__(self.value + other.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value  # Comparing values for equality

    def __str__(self):
        return f"{self.value} {self.__class__.__name__}"


    @classmethod
    def course(cls, other):
        return 1 / other.course_factor()

    @classmethod
    def course_factor(cls):
        raise NotImplementedError


class Euro(Currency):
    @classmethod
    def course_factor(cls):
        return 1.0


class Dollar(Currency):
    @classmethod
    def course_factor(cls):
        return 2.0


class Pound(Currency):
    @classmethod
    def course_factor(cls):
        return 100.0


import pytest


@pytest.mark.parametrize(
    "from_cur,to_cur,expected",
    [
        (Euro, Dollar, 110.0),
        (Euro, Pound, 120.0),
        (Euro, Euro, 100.0),
        (Dollar, Euro, 110.0),
        (Dollar, Pound, 45.0),
        (Dollar, Dollar, 170.0),
        (Pound, Dollar, 63.0),
        (Pound, Euro, 45.0),
        (Pound, Pound, 105.0),
    ],
)
def test_get_sum(from_cur, to_cur, expected):
    result = from_cur(100) + to_cur(10)
    assert float(result.value) == expected


@pytest.mark.parametrize(
    "cur1,value1,cur2,value2,expected_result",
    [
        (Dollar, 90, Euro, 45, True),
        (Dollar, 40, Pound, 40, False),
        (Pound, 18, Dollar, 1, False),
    ],
)
def test_comparison_equal(cur1, value1, cur2, value2, expected_result):
    assert (cur1(value1) == cur2(value2)) == expected_result

