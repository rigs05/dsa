"""
88. Merge Sorted Array:
- Two sorted arrays are given → merge them without disturbing the sorting
- 1st array contains n 0s after the elements get over
- Solution:
	- 
"""
from typing import List
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
			l, r = 0, 0
			tmp = []
			while l < m and r < n:
					if nums1[l] <= nums2[r]:
							tmp.append(nums1[l])
							l += 1
					else:
							tmp.append(nums2[r])
							r += 1
			
			while l < m:
					tmp.append(nums1[l])
					l += 1
			
			while r < n:
					tmp.append(nums2[r])
					r += 1
			
			for i in range(m+n):
					nums1[i] = tmp[i]


	# performs in-place changing by iterating right → left in arrays
	def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
			i, j, k = m-1, n-1, len(nums1)-1

			while j >= 0:
					if i >= 0 and nums1[i] > nums2[j]:
							nums1[k] = nums1[i]
							i -= 1
					else:
							nums1[k] = nums2[j]
							j -= 1
					k -= 1