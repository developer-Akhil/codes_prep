from typing import List


def get_median(nums: List[int]) -> float:
    list_len = len(nums)

    m = list_len - 1

    nums.sort()

    m1 = nums[list_len // 2]

    m2 = nums[m // 2]

    median = (m1 + m2) / 2

    return median


l = [1, 3, 2]

l2 = [1, 2, 4, 3,5]
print(get_median(l2))
