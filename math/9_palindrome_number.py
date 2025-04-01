"""
====
Easy
====

Given an integer x, return true if x is a palindrome, and false otherwise.

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True

    length = 1
    while x // (10 ** length) != 0:
        length += 1

    l_temp = x
    r_temp = x

    while length // 2 != 0:
        left = l_temp % 10
        right = r_temp // (10 ** (length - 1))

        if left != right:
            return False

        l_temp //= 10
        r_temp -= right * (10 ** (length - 1))

        length -= 1

    return True
