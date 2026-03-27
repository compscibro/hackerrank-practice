'''
Problem 9: Merge Strings Alternately
Write a function merge_alternately() that accepts two strings word1 and word2. Merge the
strings by adding letters in alternating order, starting with word1. If a string is longer
than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

def merge_alternately(word1, word2):
	pass

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2) # "woozle"

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2) # "heffalump"

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2) # "eeyore"