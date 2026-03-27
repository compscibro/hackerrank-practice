'''
Problem 1: String Array Equivalency
Given two string arrays word1 and word2, return True if the two arrays represent the same
string, and False otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''

def are_equivalent(word1, word2):
	pass

word1 = ["bat", "man"]
word2 = ["b", "atman"]
are_equivalent(word1, word2) # True

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
are_equivalent(word1, word2) # False

word1 = ["cat", "wom", "an"]
word2 = ["catwoman"]
are_equivalent(word1, word2) # True