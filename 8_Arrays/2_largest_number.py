# Given an array of integers nums, return the value of the largest element in the array

# Example 1:
# Input: nums = [3, 3, 6, 1]

# Output: 6

# Explanation: The largest element in array is 6

def largestElement(nums):
    n=len(nums)
    max_element=nums[0]
    for i in range(0,n):
        if max_element<nums[i]:
            max_element=nums[i]
    return max_element

nums = [3, 3, 6, 1]
print(largestElement(nums))
