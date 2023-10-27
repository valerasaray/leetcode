'''
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b = [1, 2, 3, 4, 5, 6]
median = (3 + 4) / 2 = 3.5
'''

# импортирую тип List
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        while nums1 and nums2:
            nums3.append((nums1 if nums1[-1] > nums2[-1] else nums2).pop(-1))
        nums3 = (nums3 + nums1[::-1] + nums2[::-1])[::-1]

        lengh3 = len(nums3)
        if lengh3 % 2 != 0:
            return nums3[lengh3//2]
        return (nums3[lengh3//2-1] + nums3[lengh3//2])/2

s = Solution()
print(s.findMedianSortedArrays([1, 2, 3], [4, 5, 6]))