"""
Find all the Divisors (factors) of a number
- E.g. : 18 = 1, 2, 3, 6, 9, 18
- Solution (Brute Force): O(N)
	- Iterate from 1 to N & find if N % i == 0
	- Store all the iterations that have 0 as remainder
- Solution (Optimal): O(sqrt(N))
	- Factors repeat themselves by 1 x 18, 2 x 9, 3 x 6, 6 x 3 ...
	- Factor-combination will be valid until sqrt(N) after which reversal will happen
	- If N % i == i (i.e. 6 x 6 for 36), store only 1st factor & ignore the rest
"""
import math

class Divisors:
	def logic (x: int) -> int:
		max_div = int(math.sqrt(x))
		arr = []
		for i in range(1, max_div+1):
			if x % i == 0:
				arr.append(i)
				if x / i != i:
					arr.append(int(x / i))
		arr.sort()
		return arr

if __name__ == "__main__":
	x = int(input("Enter the Number to find it's divisors: "))
	print(f"Divisors: {Divisors.logic(x)}")
