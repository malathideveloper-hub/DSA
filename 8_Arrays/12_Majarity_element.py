# Given an integer array nums of size n, 
# return the majority element of the array.

# The majority element of an array is an element 
# that appears more than n/2 times in the array. 
# The array is guaranteed to have a majority element.

# Example 1:
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

# Output: 7

# Explanation:

# The number 7 appears 5 times in the 9 sized array

def majorityElement(nums):
    d = {}

    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    n = len(nums)

    for k, v in d.items():
        if v > n // 2:
            return k

print(majorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))

# Complexity	        Value	            Reason
# Time	            O(n) average	    Two linear traversals and average O(1) dictionary operations
# Auxiliary Space	    O(n)	            Dictionary stores element frequencies