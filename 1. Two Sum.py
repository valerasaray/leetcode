'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# импортирую тип List
from typing import List

class Solution:
    # функция обхода списка с последовательным попарным сравнением всех его элементов 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# создание экземпляра класса Solution
s = Solution()

# тест решения
print(s.twoSum([1, 4, 2], 3))