# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

# Example 1:
# Input: nums = [0, 2, 3, 1, 4]

# Output: 5

# Explanation:

# nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
def missingNumber(nums):
    n=len(nums)
    for i in range(n+1):
        if i not in nums:
            return i
    
def missingNumber_optimized(nums):
    n = len(nums)

    # Sum of numbers from 0 to n
    expected_sum = sum(range(n + 1))

    # Sum of elements present in the array
    actual_sum = sum(nums)

    # Missing number
    return expected_sum - actual_sum


nums = [1, 3, 6, 4, 2, 5]

print(missingNumber(nums))  # Output: 0
# Complexity:
# - Time: O(n^2)
# - Auxiliary Space: O(1)
print(missingNumber_optimized(nums))  # Output: 0
# Complexity:
# - Time: O(n)
# - Auxiliary Space: O(1)