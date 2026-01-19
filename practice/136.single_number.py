"""
136. Single Number
- Given an array where each element except one is repeated twice
- Return the single element
- Solution:
	- Store the elements with their count in a dictionary
	- Add +1 everytime any existing element re-occurs
	- Iterate the Dictionary and return the key having value == 1
"""

from typing import List
def single_num(arr: List[int]) -> int:
		if len(arr) % 2 == 0:	# loop out if array length is even
			return

		if len(arr) == 1:
			return arr[0]

		d1 = {}
		
		for i in range(len(arr)):
			if arr[i] not in d1:
				d1[arr[i]] = 1
			else:
				d1[arr[i]] += 1
		
		for key, value in d1.items():
			if value == 1:
				return key

arr = list(map(int, input("Input array elements separated by space: ").split()))
print(f"Single out number: {single_num(arr)}")