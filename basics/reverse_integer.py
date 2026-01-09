'''
LC
7. Reverse Integer
- Conditions:
	- reverse the integer
	- reversed number must follow 32-bit integer, else print 0
- Solution:
	- capture the sign of integer
	- extraction of digit always happens right → left (using % operation)
	- to form a reverse number, the extracted value should be x10 to add the next last element and so on
	- comparison logic to check if result comes under 32-bit integer range i.e. [-2^31, 2^31 - 1]
'''

class ReverseNumber:
	def logic(x: int) -> int:
		sign = -1 if x < 0 else 1
		x = abs(x)
		rev = 0

		while x:
			rev = rev * 10 + (x % 10)
			x //= 10
		
		rev *= sign
		
		if -2**31 <= rev <= 2**31-1:
			return rev
		return 0

if __name__ == "__main__":
	x = int(input("Enter the number to be reversed: "))
	print(f"Reversed: {ReverseNumber.logic(x)}")
