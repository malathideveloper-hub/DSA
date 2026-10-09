# Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.

# Example 1:
# Input: n = 5, arr = [1,2,3,4,5]

# Output: True

# Explanation: The given array is sorted i.e 
# Every element in the array is smaller than or equals to its next values, So the answer is True.

def arraySortedOrNot(arr,n):
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
    return True


n = 5
arr = [1,2,3,4,5]

print(f"Given array {arr} is {"Sorted" if arraySortedOrNot else "Not Sorted"}")


# Remember this for DSA

# Non-decreasing: arr[i] <= arr[i + 1] — duplicates allowed.

# Strictly increasing: arr[i] < arr[i + 1] — duplicates not allowed.

# Complexity: Time O(n), auxiliary space O(1).