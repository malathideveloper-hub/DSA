# Given a binary array nums, return the maximum number of consecutive 1s in the array.

# A binary array is an array that contains only 0s and 1s.

# Example 1:
# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

# Output: 3

# Explanation:

# The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s


def findMaxConsecutiveOnes(nums):
    count=0
    max_count=0
    for i in nums:
        if i==1:
            count+=1
            if count>max_count:
                max_count=count
        else:
            count=0
    return max_count

nums = [1, 1, 0, 0, 1, 1, 1, 0]
print(findMaxConsecutiveOnes(nums))

# Time: (O(n)) — one pass through the array.
# Auxiliary space: (O(1)) — only two counters.