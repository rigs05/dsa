"""
Insertion Sort:
- Takes an element and places it in correct order
- Increase the window-size and perform adjacent comparisons inside that window until correct order is reached
- Iteration goes Right → Left
"""

def insertion_sort(arr):
	n = len(arr)
	for i in range(1, n):		# handles window-size
		j = i		# move initial pointer at the end element of the window
		while j > 0 and arr[j-1] > arr[j]:	# swap until j-1'th element remain smaller than j'th element
			arr[j-1], arr[j] = arr[j], arr[j-1]
			j -= 1

arr = list(map(int, input("Enter the array: ").split()))
insertion_sort(arr)
print(f"Sorted Array: {arr}")