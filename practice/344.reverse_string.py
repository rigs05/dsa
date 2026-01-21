"""
344. Reverse Strings (reverse in-place)
- Solution:
	- using iteration:
		- define l=0, r=len(s)-1
		- while l<r → swap 1st and last element in string
	- using recursion:
		- if i > n/2 → return
		- swap s[i] ↔︎ s[n-i-1]
		- call f(i+1)
"""

class Reverse_String:
	def iterative(self, s):
		l, r = 0, len(s) - 1
		while l < r:
			s[l], s[r] = s[r], s[l]
			l += 1
			r -= 1
	
	def recursive(self, s, i=0):
		n = len(s)
		if i > n//2:
			return
		s[i], s[n-i-1] = s[n-i-1], s[i]
		self.recursive(s, i+1)


if __name__ == "__main__":
	string_arr = list(input("Enter the string to reverse: "))
	print("1. Reverse by Iterative Method")
	print("2. Reverse by Recursive Method")
	optn = int(input("Enter the option to reverse array: "))
	print(f"Input String: {string_arr}")

	match optn:
		case 1:
			Reverse_String().iterative(string_arr)
		case 2:
			Reverse_String().recursive(string_arr, 0)
		
	print(f"Reversed String: {string_arr}")