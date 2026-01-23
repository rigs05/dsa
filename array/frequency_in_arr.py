"""
GFG. Frequencies in a Limited Array
- Given array of numbers e.g. [1, 2, 4, 2, 1]
- Output their frequencies in an array where i-th element act as index number (0-indexed)
- e.g. [2, 2, 0, 1, 0] → 1 & 2 in array repeats twice, 4 repeats once, rest are 0
- Solution:
	- Initialize a new array with 0s
	- add +1 to new_arr[arr[i]]
"""

def return_frequency_array(arr):
	n = len(arr)
	new_arr = [0] * n
	for i in range(0, n):
		new_arr[arr[i]-1] += 1
	return new_arr


arr = list(map(int, input("Enter the array: ").split()))
print(f"Original Array: {arr}")
print(f"Frequency Array: {return_frequency_array(arr)}")

