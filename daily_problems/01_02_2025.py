"""
----
Easy
----

3151. Special Array I

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
"""


def is_array_special(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True

    nums = [i % 2 for i in nums]

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return False

    return True
