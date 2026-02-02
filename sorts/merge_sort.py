"""
Merge Sort:
- Divide and Merge
- Array with single elements are already sorted
- Use recursion to divide the array until each individual array has exactly 1 element left
- We manipulate the index rather than the value itself
"""

from typing import List

class MergeSort:
	def sort(self, arr, low, high):
		if low >= high: return
		mid = (low + high) // 2
		self.sort(arr, low, mid)
		self.sort(arr, mid+1, high)
		self.merge(arr, low, mid, high)

	def merge(self, arr, low, mid, high):
		sorted = []
		l, r = low, mid+1
		while l <= mid and r <= high:
			if arr[l] <= arr[r]:
				sorted.append(arr[l])
				l += 1
			else:
				sorted.append(arr[r])
				r += 1
		while l <= mid:
			sorted.append(arr[l])
			l += 1
		while r <= high:
			sorted.append(arr[r])
			r += 1
		
		for i in range(low, high+1):
			arr[i] = sorted[i-low]
		
if __name__ == "__main__":
	a = List(map(int, input("Enter the unsorted array: ")))
	MergeSort().sort(a, 0, len(a))
