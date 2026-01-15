"""
1979. Finding GCD of Array
- Find GCD of minimum and maximum number
- find min and max
- use modulo operator to make one of those 0
- the other variable will be the GCD
"""

class GCD:
	def findGCD(self, nums):
					a = min(nums)
					b = max(nums)

					while a > 0 and b > 0:
							if a > b:
									a = a % b
							else:
									b = b % a
					
					if a == 0:
							return b
					return a
	
if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(GCD().findGCD(nums))

