# Given an array of integers nums, 
# return the second-largest element in the array. 
# If the second-largest element does not exist, return -1.

# Example 1:
# Input: nums = [8, 8, 7, 6, 5]
# Output: 7

# Explanation:
# The largest value in nums is 8, the second largest is 7

def secondLargestElement(nums):
    num=sorted(nums)
    n=len(num)
    largest=num[n-1]
    for i in range(n-1,-1,-1):
        if largest>num[i]:
            largest=num[i]
            break
    else:
        largest=-1
    return largest
# Above approach takes (O(n log n)) time and (O(n)) extra space.

nums = [8, 8, 7, 6, 5]
# nums=[10,10,10,10,10,10]
print(secondLargestElement(nums))