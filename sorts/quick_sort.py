"""
Quick Sort:
- Divide and Conquer algorithm
- Similar to Merge Sort in terms of Time Complexity: O(N.logN)
- Quick Sort takes Space Complexity of O(1) whereas Merge Sort takes O(N)
- Steps:
	- Choose a Pivot from the array (can be any element -- choose 1st for simplicity)
	- Put the chosen element to its correct position in the array by shifting all the elements smaller
	  or equal that to its left and larger ones to its right
	- Recursively call the remaining array to the left and right for quick sort operation after making 
	  the pivot element at correct position be named as 'Partition Index'
	- Usage of indices instead of space other than the Stack makes it perform in O(1) S.C.
"""

class QuickSort:
	def partition_function(self, arr, low, high):
		pivot = arr[low]
		i, j = low, high
		while i < j:		# perform the check until the two pointers cross each other
			while i <= high - 1 and arr[i] <= pivot:	# stop at element larger than the pivot
				i += 1
			while j >= low + 1 and arr[j] > pivot:		# stop at element smaller than the pivot
				j -= 1

			if i < j: arr[i], arr[j] = arr[j], arr[i]		# swap the elements if i & j haven't crossed yet

		arr[low], arr[j] = arr[j], arr[low]			# i & j crossed → swap the pivot with last elmeent i.e. at j
		return j			# return the partition index for recursive calls

	def qs(self, arr, low, high):
		if low < high:		# arrays with single elements are already sorted
			pIndex = self.partition_function(arr, low, high)
			self.qs(arr, low, pIndex-1)
			self.qs(arr, pIndex+1, high)


if __name__ == "__main__":
	arr = list(map(int, input("Enter elements separated by space: ").split()))
	qs_obj = QuickSort()
	qs_obj.qs(arr, 0, len(arr) - 1)
	print("Sorted array:", arr)