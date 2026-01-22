"""
125. Valid Palindrome String
- given an Alphanumeric, All-case string/statement, check if it's a palindrome
- Solution (Iterative):
	- convert the string to lowercase, remove alphanumeric symbols
	- use in-built isalnum() with join or re library to remove the symbols
	- use two-pointer approach (l, r)
	- compare until they collide
"""

def isPalindrome(s):
	# convert the given string to lowercase → removed symbol → joined together → made into a list
	clean = list(''.join(c.lower() for c in s if c.isalnum()))
	l, r = 0, len(clean) - 1
	while l < r:
		if clean[l] == clean[r]:
			l += 1
			r -= 1
		else:
			return False
	return True


stmt = str(input("Enter the statement to check if palindrome: "))
if isPalindrome(stmt):
	print("The statement is a palindrome")
else:
	print("The statement is not a palindrome")

