"""
- Recursion is calling of a function again and again
- BASE Condition/Specified Condition: decides when will the function execution complete
- Recursion Tree: Graphical Representation of recursion defined in the form of F(X)
- Stack Overflow/Stack Space/Auxiliary Space: place where incompleted functions are stored
- Stack Space is the machine's internal memory consumption by a program using it's Stack
- Count variables should be passed on using parameters only

- Note: IDENTIFY the task that recursion needs to do in order to find the recursion logic & base condition
"""
class Recursion:
	# 1. Print Name 5x
	def printName(self, name, cnt=1):
		if cnt > 5:
			return
		print(f"{cnt}.{name}")
		self.printName(name, cnt + 1)
	
	# 2. Print 1 → N
	def print_till_N(self, n, count=1):
		if count > n:
			return
		print(count)
		self.print_till_N(n, count + 1)

	# 3. Print N → 1
	def print_rev(self, n):
		if n < 1:
			return
		print(n)
		self.print_rev(n - 1)

	# 4. Print 1 → N using Backtracking
	def print_backtrack(self, n):
		if n < 1:
			return
		self.print_backtrack(n-1)
		print(n)		# Note the print comes AFTER the recursion is called and not before
	
	# 5. Print N → 1 using Backtracking
	def print_backtrack_back(self, n, i=1):
		if i > n:
			return
		self.print_backtrack_back(n, i+1)
		print(i)

if __name__ == "__main__":
	print("1. Print Certain Name 5 times")
	print("2. Print Linearly from 1 to N")
	print("3. Print from N to 1")
	print("4. Print Linearly from 1 to N (using Backtracking)")
	print("5. Print Linearly from N to 1 (using Backtracking)")

	trigger = int(input("Choose what to perform: "))
	match trigger:
		case 1:
			name = input("Enter the name to print: ")
			Recursion().printName(name)
		case 2:
			n = int(input("Enter N to print 1 → N: "))
			Recursion().print_till_N(n)
		case 3:
			n = int(input("Enter N to print N → 1: "))
			Recursion().print_rev(n)
		case 4:
			# Backtracking refers to Starting from N → Base Condition returns the function call 
			# → Actual Logic is executed (i.e. print from 1 → N)
			n = int(input("Enter N to print 1 → N using Backtracking: "))
			Recursion().print_backtrack(n)
		case 5:
			n = int(input("Enter N to print N → 1 using Backtracking: "))
			Recursion().print_backtrack_back(n)