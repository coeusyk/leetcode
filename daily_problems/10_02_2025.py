"""
----
Easy
----

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:
- Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.
"""


def clear_digits(s: str) -> str:
    i = 1

    while i < len(s):
        if s[i].isdigit() and s[i - 1].isalpha():
            s = s[:i - 1] + s[i + 1:]
            i = max(1, i - 2)

        else:
            i += 1

    return s
