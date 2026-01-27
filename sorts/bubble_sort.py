"""
Bubble Sort:
- Opposite of selection sort where we swap the Largest element to the end
- Push the elements to the end by ADJACENT SWAPPING
- Time Complexity: O(N^2) {Worst, Average Case} ; O(N) {Best Case}
- Best Case complexity will happen if the array is already sorted (verified by a is_swapped flag)
- Iteration goes Left → Right
"""

def bubble_sort(arr):
	n = len(arr)
	is_swapped = 0
	for i in range(n-1, 0, -1):	 	# reduce the iter size from last upto 2nd from start element
		for j in range(0, i, 1):		# iterate each range till i-1 to compare adjacent elements
			if arr[j] > arr[j+1]:				# if RHS > LHS → SWAP
				arr[j], arr[j+1] = arr[j+1], arr[j]
				is_swapped = 1
		if not is_swapped:
			break

arr = list(map(int, input("Enter the array: ").split()))
bubble_sort(arr)
print(f"Sorted Array: {arr}")