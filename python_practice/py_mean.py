from typing import List


def mean(nums: List[int]) -> float:
    leng_list = len(nums)

    sum_list = sum(nums)

    mean_result = sum_list / leng_list

    return mean_result


nums = [1, 2, 3, 4, 5,6]
print(mean(nums))
