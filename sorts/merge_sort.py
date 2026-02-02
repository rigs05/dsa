"""
Merge Sort:
- Divide and Merge
- Array with single elements are already temp
- Use recursion to divide the array until each individual array has exactly 1 element left
- We manipulate the index rather than the value itself
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

if __name__ == "__main__":
	a = list(map(int, input("Enter the unsorted array: ").split()))
	MergeSort().sort(a, 0, len(a)-1)
	print(f"Sorted Array: {a}")
