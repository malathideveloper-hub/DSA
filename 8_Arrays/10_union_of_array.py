# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.
# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.
# Example 1:
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
# Output: [1, 2, 3, 4, 5, 7]
# Explanation:
# The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

def findUnion(nums1, nums2):

    result = []

    i = 0
    j = 0

    # Compare elements while both arrays have elements
    while i < len(nums1) and j < len(nums2):

        if nums1[i] == nums2[j]:

            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])

            i += 1
            j += 1

        elif nums1[i] < nums2[j]:

            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])

            i += 1

        else:

            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])

            j += 1

    # Process remaining elements in nums1
    while i < len(nums1):

        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])

        i += 1

    # Process remaining elements in nums2
    while j < len(nums2):

        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])

        j += 1

    return result


nums1 = [1, 2, 2, 3]
nums2 = [4, 5, 6, 6]

print(findUnion(nums1, nums2))

# Complexity analysis
# Let n be the length of nums1 and m be the length of nums2.

# Complexity	    Value	        Reason
# Time	            O(n + m)	    Each pointer moves forward at most through its array once
# Auxiliary space	O(1)	        Excluding the output array
# Output space	    O(n + m)	    Stores the union