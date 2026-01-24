"""
Selection Sort
- 2 Nested Loops
- SELECT the minimum element from INNER loop → Swap with element at idx. of OUTER loop
- ONE swap per outer iteration
- test (24-01-2026 - on the roof)
"""

def selection_sort(arr):
	n = len(arr)
	for i in range(n):
		min_idx = i  # Using local variable to store index number to MINIMIZE swapping
		for j in range(i+1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i] # perform swapping after finding the MINIMUM number

arr = list(map(int, input("Enter the unsorted array: ").split()))
selection_sort(arr)
print(f"Sorted Array: {arr}")
