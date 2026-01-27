"""
3042. Count Prefix and Suffix Pairs - 1:
- given an array of words, if any set of the given words are prefix and suffix of one-another, it counts as a pair
- return total number of such pairs
- Solution:
	- A separate bool function that checks if both prefix & suffix for 2 words are true
	- Nested loop to select all the possible combination of words from the given array
	- Ensure i != j and words[i] < words[j]
 	- Increase Count as the bool function returns True
"""

from typing import List
class Prefix_and_Suffix:
	def pairs(self, words: List[str]) -> int:
		count = 0
		n = len(words)
		for i in range(n):
			for j in range(i+1, n):
				a, b = words[i], words[j]
				if len(a) > len(b):
					continue
				if b.startswith(a) and b.endswith(a):
					count += 1
		return count
	

if __name__ == "__main__":
	ar = list(map(str, input("Enter the array of strings to find their pairs: ").split()))
	print(f"Total no. of pairs: {Prefix_and_Suffix().pairs(ar)}")
