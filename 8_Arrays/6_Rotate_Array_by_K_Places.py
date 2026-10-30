# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2

# Output: nums = [3, 4, 5, 6, 1, 2]

# Explanation:

# rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

def rotateArray(nums, k: int) -> None:
    # nums = [3, 4, 1, 5, 3, -5]
    # k = 8

    #Take the proper rotation count
    k=k%len(nums)
    # print(k)

    #take the elemetns on a temporrary array
    temp=list()
    for i in range(0,k):
        temp.append(nums[i])
    # print(temp)

    #insert the remaing elements on the first of the array - shift it to left
    n=len(nums)
    j=0
    for i in range(k,n):
        nums[j]=nums[i]
        j+=1
    # print(nums)

    #insert the temp - rotation
    j=0
    for i in range((n-k),n):
        nums[i]=temp[j]
        j+=1
        
    # print(nums)
    # return nums

nums = [3, 4, 1, 5, 3, -5]
k = 8
rotateArray(nums,k)
print(nums)

# Complexity:
# - First loop: (O(k))
# - Second loop: (O(n-k))
# - Third loop: (O(k))
# - Temporary array: (O(k)) extra space.
# Overall time: (O(n)).

# Complexity
# Time = (O(n))
# Auxiliary space = (O(k))