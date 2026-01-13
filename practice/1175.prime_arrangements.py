"""
1175. Prime Arrangements (https://leetcode.com/problems/prime-arrangements/description/)
- Problem:
	- Return the number of permutations of prime numbers being placed at prime positions
	- Reduce the result to 10^9 + 7 form for large numbers
- Solution:
	- Find all the prime numbers between 1 - N
	- prime numbers = prime positions = numbers can be interchanged in those locations
	- similarly non-prime numbers can be interchanged as well
	- overall permutation requires rearranging ALL of the permutation sets i.e. both for prime & composite
	- that's why res = P! * (N-P)!
	- return res % 10^9 + 7 (as given)
"""
import math
class Arrangements:
	def numPrimeArrangements(self, n: int) -> int:
		prime = 0
		for i in range(1, n+1):
			if self.isPrime(i) == True:
				prime += 1
			
		# Find overall permutation
		res = math.factorial(prime) * math.factorial(n - prime)
		return res % (10**9 + 7)

	# Find if number is prime
	def isPrime(self, x):
		if x < 2:		# any number less than 2 is not a prime
			return False
		for j in range(2, int(math.sqrt(x))+1):
			if x % j == 0:
				return False		# iterating between 2 & sqrt(X) → NO factors should be there for the number to be prime
		return True
	

if __name__ == "__main__":
	print("Find the permutations of prime positions...")
	x = int(input("Enter the number to find it's combinations: "))
	solve = Arrangements()
	print(f"No. of Arrangements possible: {solve.numPrimeArrangements(x)}")
