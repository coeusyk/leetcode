"""
[2873] Maximum Value of an Ordered Triplet I

--- Easy ---

You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
"""


def maximum_triplet_value(nums: list[int]) -> int:
    n = len(nums)
    max_value = 0

    for i in range(n - 2):
        min_j = nums[i + 1]

        for j in range(i + 1, n - 1):
            if nums[j] <= min_j:
                min_j = nums[j]
            else:
                continue

            if nums[i] <= nums[j]:
                continue

            max_k = nums[j + 1]

            for k in range(j + 1, n):
                if nums[k] >= max_k:
                    max_k = nums[k]

                    value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(value, max_value)

    return max_value


print(maximum_triplet_value([1,10,3,4,19]))
