"""
Find if given number is Armstrong Number
- Sample: 371 = 3*3*3 + 7*7*7 + 1*1*1 = 27 + 343 + 1 = 371
- Solution:
	- 
"""

class Armstrong:
	def logic(x:int) -> bool:
		num = 0
		dup = x
		while x:
			num += (x%10)**3
			x //= 10
		if num == dup:
			return True
		else:
			return False
		

if __name__ == "__main__":
	x = int(input("Enter the number: "))
	print("Armstrong Number") if Armstrong.logic(x) == True else print("Not an Armstrong Number")