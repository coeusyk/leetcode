"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.
"""


def majority_element(nums: list[int]) -> int:
    hash_map = {}

    for n in nums:
        if n not in hash_map:
            hash_map[n] = 1
        else:
            hash_map[n] += 1

        if hash_map[n] > (len(nums) // 2):
            return n
