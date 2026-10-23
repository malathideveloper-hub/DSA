# Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

# Example 1:
# Input: nums = [7, 4, 1, 5, 3]

# Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7.

# Thus the array is sorted in non-decreasing order.


nums = [5, 3, 4, 1, 2]
n = len(nums)

for i in range(1, n):
    key = nums[i]
    j = i - 1

    # Shift larger elements to the right
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    # Insert key into its correct position
    nums[j + 1] = key

print(nums)