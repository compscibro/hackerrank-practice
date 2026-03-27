'''
Problem 8: Left and Right Sum Differences
Given a 0-indexed integer array nums, write a function left_right_difference() that returns
a 0-indexed integer array answer where:

len(answer) == len(nums)
answer[i] = left_sum[i] - right_sum[i]

Where:
left_sum[i] is the sum of elements to the left of index i in nums. If there is no such
element, left_sum[i] = 0.
right_sum[i] is the sum of elements to the right of index i in nums. If there is no such
element, right_sum[i] = 0.
'''

def left_right_difference(nums):
	pass

nums = [10, 4, 8, 3]
left_right_difference(nums) # [-15, -1, 11, 22]

nums = [1]
left_right_difference(nums) # [0]