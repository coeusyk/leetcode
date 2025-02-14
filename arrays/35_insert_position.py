"""
----
Easy
----

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


def search_insert(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return start
