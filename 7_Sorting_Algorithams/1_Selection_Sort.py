# Given an array of integers nums, sort the array in 
# non-decreasing order using the selection sort algorithm 
# and return the sorted array.
# A sorted array in non-decreasing order is an array 
# where each element is greater than or equal to all 
# previous elements in the array.

# Example 1:
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

def selectionSort(nums):
        n=len(nums)
        for i in range(0,n):
            mini=nums[i]
            index=i
            for j in range(i+1,n):
                if mini>nums[j]:
                    mini=nums[j]
                    index=j
            nums[i], nums[index] = nums[index], nums[i]
        return nums


nums = [7, 4, 1, 5, 3]
print(selectionSort(nums))