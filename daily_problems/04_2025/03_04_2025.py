"""
[2874] Maximum Value of an Ordered Triplet II

--- Medium ---

You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""


def maximum_triplet_value_v2(nums: list[int]) -> int:
    n = len(nums)

    left_max = [0] * n
    right_max = [0] * n

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i - 1])
        right_max[n - i - 1] = max(right_max[n - i], nums[n - i])

    max_value = 0

    for j in range(1, n - 1):
        max_value = max(max_value, (left_max[j] - nums[j]) * right_max[j])

    return max_value
