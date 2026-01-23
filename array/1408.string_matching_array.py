"""
1408. String Matching in an Array
- return all substrings in an array of strings
- input: words = ["mass","as","hero","superhero"]
- Solution:
	- O(n^2.m) time complexity ; O(1) space complexity
	- Nested loops iterating same array → push the matching words in separate array
"""

def find_substring(words):
	sub = []
	for i in range(len(words)):
		for j in range(len(words)):
			if i != j and words[i] in words[j]:
				sub.append(words[i])
				break
	return sub

words_list = list(map(str, input("Enter the words array: ").lower().split()))
print(f"Words list: {words_list}")
print(f"Substrings in list: {find_substring(words_list)}")
