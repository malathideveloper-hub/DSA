# Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.

# In Pascal's triangle:

# The first row contains a single element 1.
# Each row has one more element than the previous row.
# Every row starts and ends with 1.
# For all interior elements (i.e., not at the ends), the value at position (r, c) is computed as the sum of the two elements directly above it from the previous row:

# Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
# where indexing is 1-based
# Example 1:
# Input: r = 4, c = 2

# Output: 3

# Explanation:

# The Pascal's Triangle is as follows:

# 1

# 1 1

# 1 2 1

# 1 3 3 1

# Thus, value at row 4 and column 2 = 3


def pascalElement(r, c):
    n = r - 1
    k = c - 1

    # Use symmetry to minimize iterations
    k = min(k, n - k)

    result = 1

    for i in range(1, k + 1):
        result = result * (n - i + 1) // i

    return result


r = 5
c = 3

print(pascalElement(r, c))

# Complexity
# - Time: (O(min(c-1, r-c)))
# - Auxiliary space: (O(1))