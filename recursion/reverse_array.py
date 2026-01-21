"""
Reverse an Array using Recursion:
- common way to do that is using for/while loop
- take two pointer, one at beginning index, and one at the end
- swap the elements until left pointer crosses the right one (perform l+1, r-1)
- recursion will have similar logic (using 2 pointers)

Reversing the Array using single variable:
- perform swapping between i and N using (N - i - 1)
- if i crosses N/2, stop
"""

class Reverse_Arr:
	def one_ptr(self, arr, i=0):
		n = len(arr)
		if i >= n//2:
			return
		arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
		self.one_ptr(arr, i+1)

	def two_ptr(self, arr, l, r):
		if l >= r:
			return
		arr[l], arr[r] = arr[r], arr[l]
		self.two_ptr(arr, l+1, r-1)

		
if __name__ == "__main__":
	arr = list(map(int, input("Enter array separated by space: ").split()))

	print("1. Reverse using One-Pointer (n-i-1) approach")
	print("2. Reverse using Two-Pointer (l+1, r-1) approach")
	optn = int(input("Enter the option to reverse array: "))
	print(f"Input Array: {arr}")

	match optn:
		case 1:
			Reverse_Arr().one_ptr(arr)
		case 2:
			Reverse_Arr().two_ptr(arr, 0, len(arr)-1)
			
	print(f"Reversed Array: {arr}")