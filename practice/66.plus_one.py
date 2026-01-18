"""
66. Plus One
- given array of integer elements, return array with +1
- e.g. [1, 2, 3] → [1, 2, 4] ; [9] → [1, 0]
- return -1 if array is not of numbers
"""

from typing import List
def addOne(arr: List[int]) -> List[int]:
	for i in range(len(arr)-1, -1, -1):
		if arr[i] < 9:
			arr[i] += 1
			return arr
		arr[i] = 0
	return [1] + arr

def addOne2nd(arr: List[int]) -> List[int]:
	return list(map(int, str( int(''.join(map(str, arr))) + 1) ))


if __name__ == "__main__":
	arr = list(map(int, input("Enter the array (separated by space): ").split()))
	print(f"Array: {arr}")
	# print(f"updated Array: {addOne1st(arr)}")
	print(f"Updated Array: {addOne2nd(arr)}")