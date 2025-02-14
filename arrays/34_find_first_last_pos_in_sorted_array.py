"""
------
Medium
------

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given
target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


def search_range(nums: list[int], target: int) -> list[int]:
    if len(nums) == 0:
        return [-1, -1]

    start = 0
    end = len(nums) - 1

    target_start = -1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            target_start = mid
            end = mid - 1

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    start = target_start
    end = len(nums) - 1

    target_end = -1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            target_end = mid
            start = mid + 1

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return [target_start, target_end]


print(search_range([1, 2, 3], 1))
