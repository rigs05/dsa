"""
Check if number is Prime
- prime number has exactly 2 factors, 1 and the number itself
- Solution:
	- Brute force: O(N)
		- Iterate from 1 → N to check if N % i == 0, increase count if True
		- Check count if 2, then Number is Prime, else Not
	- Optimal: O(sqrt(N))
		- Every number's prime number can be within the sqrt(N) range
		- Count the factors
		- Check if count is 2 or more than 2
"""
import math
class Is_Prime:
	def logic(x: int) -> bool:
		count = 0
		for i in range(1, int(math.sqrt(x))+1):
			if x % i == 0:
				count += 1
				if x / i != i:
					count += 1
		if count == 2:
			return True
		return False
	
if __name__ == "__main__":
	print("Check if number is prime or not...")
	x = int(input("Enter the number: "))
	if Is_Prime.logic(x) == True:
		print("Number is Prime")
	else:
		print("Number is NOT Prime")
