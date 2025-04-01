"""
[2460] Apply Operations to an Array

--- **Easy** ---

You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following
on the ith element of nums:

- If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.

- For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

Return the resulting array.

**Note** that the operations are applied sequentially, not all at once.
"""


def apply_operations(nums: list[int]) -> list[int]:
    i = 0
    moved_zeros = 0

    while i < len(nums) - moved_zeros - 1:
        if sum(nums[i:]) == 0:
            break

        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

            nums.remove(0)
            nums.append(0)

            moved_zeros += 1

        i += 1

    if 0 in nums:
        start_index = nums.index(0)

        while start_index < len(nums) - moved_zeros - 1:
            if nums[start_index] == 0:
                nums.remove(0)
                nums.append(0)

                moved_zeros += 1
                start_index -= 1

            start_index += 1

    return nums
