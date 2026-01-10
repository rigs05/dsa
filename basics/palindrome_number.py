"""
9. Palindrome Number
- Solution:
	- Find reverse of a number (negative numbers will always be non-palindrome)
	- compare with original number
"""

class Palindrome:
	def logic(x: int) -> int:
		num = x  # store the original value
		rev = 0
		if x < 0:
			return False
		while x:
			rev = rev * 10 + x % 10
			x //= 10
		
		if num == rev and -2**31 <= rev <= 2**31-1:
			return True
		else:
			return False

if __name__ == "__main__":
	x = int(input("Enter the number to find its palindrome: "))
	is_palindrome = Palindrome.logic(x)
	if is_palindrome:
		print("Number is a palindrome number")
	else:
		print("Number is not a palindrome")