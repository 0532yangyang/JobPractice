# -*- coding: utf-8 -*-



def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums = sorted(enumerate(nums), key=lambda x: x[1])    # TODO 学习一下这种用法
    low = 0
    high = len(nums) - 1
    while low < high:
        if nums[low][1] + nums[high][1] < target:
            low += 1
        elif nums[low][1] + nums[high][1] > target:
            high -= 1
        else:
            return [nums[low][0], nums[high][0]]
    return None


if __name__ == '__main__':
    pass