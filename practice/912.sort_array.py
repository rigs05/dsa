"""
912.Sort Array using Merge Sort O(N.LogN) time complexity
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i = j = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])

        return merged
