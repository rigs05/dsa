"""
Factorial of a number N:
- 5! = 5 x 4 x 3 x 2 x 1
- Solution:
	- Use functional recursion
"""

class Fact:
	def factorial(self, x, fact=1):
		if x == 1:
			return fact
		return self.factorial(x-1, fact * x)
	
	def fact_2(self, x):
		if x == 1:
			return 1
		return x * self.fact_2(x-1)
		

n = int(input("Enter number to find its factorial: "))
print(f"Factorial of {n} using functional way = {Fact().factorial(n)}")
print(f"Factorial of {n} using parameterized way = {Fact().fact_2(n)}")