"""
Merge Sort:
- Divide and Merge
- Array with single elements are already temp
- Use recursion to divide the array until each individual array has exactly 1 element left
- We manipulate the index rather than the value itself
- Two Types:
	- Index-based sorting
	- Slice-based sorting
	- test (07-02-2026)
	- test2 (08-02-2026)
	- test3 (09-02-2026)
	- test4 (10-02-2026)
	- test5 (11-02-2026)
	- test6 (12-02-2026)
	- test7 (13-02-2026)
	- test8 (14-02-2026)
	- test9 (15-02-2026)
	- test10 (16-02-2026)
	- test11 (17-02-2026)
"""

class MergeSort:
	def sort(self, arr, low, high):
		if low >= high: return
		mid = (low + high) // 2
		self.sort(arr, low, mid)
		self.sort(arr, mid+1, high)
		self.merge(arr, low, mid, high)

	def merge(self, arr, low, mid, high):
		temp = []
		l, r = low, mid+1
		# compare smallest elements from the two arrays & put in temp array
		while l <= mid and r <= high:
			if arr[l] <= arr[r]:
				temp.append(arr[l])
				l += 1
			else:
				temp.append(arr[r])
				r += 1
		# if right array ends first, put the remaining elements from left array in temp
		while l <= mid:
			temp.append(arr[l])
			l += 1
		
		# if left array ends first, put the remaining elements from right array in temp
		while r <= high:
			temp.append(arr[r])
			r += 1
		
		# iterate till the whole initial array (left arr + right arr) and put the substitute the values with sorted ones
		for i in range(low, high+1):
			arr[i] = temp[i-low]

	def slice_based_merge(self, nums):
		if len(nums) <= 1:
				return nums
		mid = len(nums) // 2
		left = self.slice_based_merge(nums[:mid])
		right = self.slice_based_merge(nums[mid:])
		
		return self.slice_merge(left, right)

	def slice_merge(self, left, right):
			i = j = 0
			merged = []
			
			while i < len(left) and j < len(right):
					if left[i] <= right[j]:
							merged.append(left[i])
							i += 1
					else:
							merged.append(right[j])
							j += 1
			
			merged.extend(left[i:])
			merged.extend(right[j:])
			return merged

if __name__ == "__main__":
	a = list(map(int, input("Enter the unsorted array: ").split()))
	MergeSort().sort(a, 0, len(a)-1)
	print(f"Sorted Array: {a}")
