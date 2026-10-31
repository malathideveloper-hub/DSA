# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.

# This must be done in place, without making a copy of the array.

# Example 1:
# Input: nums = [0, 1, 4, 0, 5, 2]

# Output: [1, 4, 5, 2, 0, 0]

# Explanation:

# Both the zeroes are moved to the end and the order of the other elements stay the same

nums = [0, 1, 4, 0, 5, 2]

j = 0
n=len(nums)
for i in range(n):
    if nums[i] != 0:
        # Place non-zero element at position j
        nums[j]=nums[i]
        # Increment j
        j+=1
# Fill remaining positions with zero

for i in range(j,n):
    nums[i]=0
    
print(nums)