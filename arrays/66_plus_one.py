"""
----
Easy
----

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to the least significant in left-to-right order. The large
integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


def plus_one(digits: list[int]) -> list[int]:
    num = 0

    for index, value in enumerate(digits):
        num += value * (10 ** (len(digits) - index - 1))

    num += 1

    return [int(i) for i in str(num)]


print(plus_one([9]))
