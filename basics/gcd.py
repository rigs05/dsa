"""
Greatest Common Divisor / Highest Common Factor (GCD/HCF)
- Given 2 numbers
- Find the highest common factor that divides both
- Brute Force:
	- Solve by iteration from 1 -> min(a, b)
- Better Approach:
	- Euclidean Formula: GCD(a,b) = GCD(a-b, b) where a > b
- Optimal Approach:
	- Modified Euclidean (to reduce no. of steps) = GCD(a,b) = GCD(a % b, b) where a > b
	- Go till one of them becomes 0, then the other one will be the HCF
- There will ALWAYS be an HCF/GCD as 1 divides every number equally

"""

class GCD:
	def logic(a, b):
		while a > 0 and b > 0:
			if a > b:
				a = a % b
			else:
				b = b % a
		
		if a == 0:
			return b
		return a
	
	def recursive(self, a, b):
		if a == 0:
			return b
		elif b == 0:
			return a
		while a > 0 and b > 0:
			if a > b:
				self.recursive(a-b, b)
			else:
				self.recursive(b-a, a)
	

if __name__ == "__main__":
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	# print(f"GCD of a and b = {GCD.logic(a, b)}")
	print(f"GCD of a and b by recursion = {GCD.logic(a, b)}")
