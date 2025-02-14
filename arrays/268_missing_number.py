def missing_number(nums: list[int]) -> int:
    sum_nums = (len(nums) * (len(nums) + 1)) // 2
    return sum_nums - sum(nums)
