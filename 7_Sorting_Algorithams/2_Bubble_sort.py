# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

# Example 1:
# Input: nums = [7, 4, 1, 5, 3]

# Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7.

# Thus the array is sorted in non-decreasing order

def bubbleSort(nums):
    n=len(nums)

    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
        
    return nums

nums = [7, 4, 1, 5, 3]
print(bubbleSort(nums))