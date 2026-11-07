# Given an integer array nums, return a list of all the leaders in the array.

# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

# Example 1:
# Input: nums = [1, 2, 5, 3, 1, 2]

# Output: [5, 3, 2]

# Explanation:

# 2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]


def leaders(nums):
    l=float('-inf')
    result=list()
    for i in nums[::-1]:
        if l<i:
            l=i
            result.append(l)
            
    return result[::-1]

nums=[1, 2, 5, 3, 1, 2]
print(leaders(nums))

# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n), including the reversed input copy.
        