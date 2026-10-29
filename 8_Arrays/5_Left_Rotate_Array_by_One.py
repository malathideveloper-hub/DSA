# Given an integer array nums, rotate the array to the left by one.

# Note: There is no need to return anything, just modify the given array.

# Example 1:
# Input: nums = [1, 2, 3, 4, 5]

# Output: [2, 3, 4, 5, 1]

# Explanation:

# Initially, nums = [1, 2, 3, 4, 5]

# Rotating once to left -> nums = [2, 3, 4, 5, 1]

def rotateArray(nums):
    n = len(nums)

    # Step 1: Save the first element
    temp=nums[0]

    # Step 2: Shift the remaining elements to the left
    n=len(nums)
    j=0
    for i in range(1,n):
        nums[j]=nums[i]
        j+=1
    # print(nums)

    # Step 3: Put the saved element at the end
    nums[n-1]=temp
    
    # print(nums)


nums = [1, 2, 3, 4, 5]
rotateArray(nums)
print(nums)

# Complexity
# - Time: (O(n)) — one pass through the array.
# - Auxiliary space: (O(1)) — only a fixed number of extra variables.