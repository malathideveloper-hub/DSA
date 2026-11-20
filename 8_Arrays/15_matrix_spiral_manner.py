# Given an M * N matrix, print the elements in a clockwise spiral manner.

# Return an array with the elements in the order of their appearance when printed in a spiral manner.

# Example 1:
# Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Explanation:

# The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

def spiralOrder(matrix):
    colBegin = 0
    colEnd = len(matrix[0]) - 1
    rowBegin = 0
    rowEnd = len(matrix) - 1

    res = []

    while rowBegin <= rowEnd and colBegin <= colEnd:

        # 1. Traverse left to right
        for i in range(colBegin, colEnd + 1):
            res.append(matrix[rowBegin][i])
        rowBegin += 1

        # 2. Traverse top to bottom
        for j in range(rowBegin, rowEnd + 1):
            res.append(matrix[j][colEnd])
        colEnd -= 1

        # 3. Traverse right to left
        if rowBegin <= rowEnd:
            for k in range(colEnd, colBegin - 1, -1):
                res.append(matrix[rowEnd][k])
            rowEnd -= 1

        # 4. Traverse bottom to top
        if colBegin <= colEnd:
            for l in range(rowEnd, rowBegin - 1, -1):
                res.append(matrix[l][colBegin])
            colBegin += 1

    return res


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiralOrder(matrix))