"""
Sum of first N numbers using recursion:
- Parameter-wise way
- Functional way
"""

class Sum_Recursion:
	## Parameterized Way
	def parameter_sum(self, n, sum=0):
		if n < 1:
			return sum	# print the sum at the end
		return self.parameter_sum(n-1, sum + n)	# iterate recursively

	## Functional Way
	def func_way(self, n):
		if n == 1:
			return 1		# inner-most loop will return 1 so that 2nd last loop ends doing 2+1 and so on
		return n + self.func_way(n-1)
	
if __name__ == "__main__":
	n = int(input("Enter N upto which sum to be performed: "))
	print(f"Parameterized Way: {Sum_Recursion().parameter_sum(n)}")
	print(f"Functional Way: {Sum_Recursion().func_way(n)}")
