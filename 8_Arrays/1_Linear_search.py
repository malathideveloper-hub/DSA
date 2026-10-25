# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

# Example 1:
# Input: nums = [2, 3, 4, 5, 3], target = 3

# Output: 1

# Explanation:

# The first occurence of 3 in nums is at index 1


def linearSearch(nums, target):
    n=len(nums)
    index=-1
    for i in range(0,n):
        if nums[i]==target:
            index=i
            break

    return index

nums = [2, 3, 4, 5, 3]
target = 3

print(linearSearch(nums,target))