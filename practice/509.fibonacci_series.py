"""
509. Fibonacci Series (Recursion)
- Logic: fib(n) = fib(n-1) + fib(n-2)
- Solution:
	- Functional Way:
		- define static return for n=1 and n=2
		- call (fib(n-1) + fib(n-2)) recursively
	- Parametized Way:
		- define parameters fib(n, a=0, b=1)
		- iterate till n < 1 → print/return the value 'a'
		- call fib(n-1, b, a+b) recursively
"""

class Fibonacci:
	def parameterized(self, n, a=0, b=1):
		if n < 1:
			return a
		return self.parameterized(n-1, b, b+a)
	
	def functional(self, n):
		if n == 1 or n == 2:
			return 1
		return self.functional(n-1) + self.functional(n-2)

if __name__ == "__main__":
	n = int(input("Enter N of fibonacci series: "))
	print(f"The Fibonacci Series Sum using Parameterized = {Fibonacci().parameterized(n)}")
	print(f"The Fibonacci Series Sum using Functional = {Fibonacci().functional(n)}")