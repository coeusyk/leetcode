"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned
integer should be non-negative as well.

You must not use any built-in exponent function or operator.
- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


def my_sqrt(x: int) -> int:
    if x == 0:
        return 0

    max_diff_from_root = 2
    max_distance_from_diff = 1

    times_max_diff_updated = 0

    while True:
        if (x - max_distance_from_diff) > max_diff_from_root:
            times_max_diff_updated += 1
            max_distance_from_diff += 1

            max_diff_from_root += (2 * (times_max_diff_updated + 1))

        else:
            return max_distance_from_diff
