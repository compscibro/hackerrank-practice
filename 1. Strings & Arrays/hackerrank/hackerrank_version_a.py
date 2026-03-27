'''
Q1: What is the output of the following code snippet?
'''
name = "codepath"
name[0] = "C"
print(name)


'''
Q2: What is the output of the following code snippet?
'''
def mystery_function(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
    return count
result = mystery_function("AABBAB")
print(result)


'''
Q3 : What is the output of the following code snippet?
'''
def mystery_function(lst, threshold):
    total = 0
    i = 0
    while i < len(lst) and total + lst[i]:
        total += lst[i]
        i += 1
    return total

result = mystery_function([1, 2, 3, 4, 5], 7)
print(result)


'''
Q4: Find The Bug: The provided code incorrectly implements the function
reverse_lst() which should accept a list lst and return the original list
with the elements in reverse order.

    def reverse_lst(lst):
        left = 0
        right = len(lst) - 1

        while left < right:
            lst[left] = lst[right]
            lst[right] = lst[left]
            left -= 1
            right += 1

        return lst

    lst = [1, 2, 3, 4, 5]
    print(reverse_lst(lst))

Identify the bug(s) within the given implementation and select the corrected
code that will successfully reverse the list.
'''
def reverse_lst(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left] = lst[right]
        lst[right] = lst[left]
        left -= 1
        right += 1

    return lst

lst = [1, 2, 3, 4, 5]
print(reverse_lst(lst))


'''
Q5: Unique - Given a string s, return True if every character in the string is
unique. Return False if any characters in S are repeated.

    Example 1
    Input: s = "abcdef"
    Expected Output: True

    Example 2
    Input: s = "aabbcc"
    Output: False

    Example 3
    Input: s = ""
    Output: True
'''
def has_all_unique_characters(s):
    pass


'''
Q6: Needle in Haystack - Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "sadbutsad",
    needle = "sad"
    Output: 0
    Explanation: "sad" occurs twice, starting at indices o and 6.
    The first occurrence is at index 0, so we return o

    Example 2:
    Input: haystack = "leetcode",
    needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

    Example 3:
    Input: haystack = "mad" needle
    = "madden"
    Needle is longer than haystack, so we return -1.
'''
def find_needle(haystack, needle):
    pass


'''
Q7: Flowerbed - You have a single long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted directly adjacent to another flower.
Given an integer array fLowerbed containing O's and 1s, where 0 means empty and 1 means 
not empty, and an integer n, return True if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and False otherwise.

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True

    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False

Hint: When deciding where to plant a new flower, focus on each plot in the flowerbed and check 
its neighboring plots. You only need to consider the plot directly before and directly after 
the current plot to determine if a flower can be planted there. Remember that the flowerbed is 
linear, so you don't need to worry about wrapping around.
'''
def can_place_flowers(flowered, n):
    pass
