# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

# Example 1:
# Input: n=5, arr = [1,2,3,4,5]

# Output: [5,4,3,2,1]

# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

def reverse(arr: list, n: int) -> None:
    # print(id(arr))
    left=0
    right=n-1
    while left < right:
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left+=1
        right-=1

n=5
arr = [1,2,3,4,5]
print(f"Before Reverse : {arr}")
reverse(arr,n)
# print(id(arr))
print(f"After Reverse : {arr}")


# Remember:
# Python also supports swapping in one line:
# arr[left], arr[right] = arr[right], arr[left]

# Time complexity: O(n)
# Auxiliary space: O(1)
# Loop condition: left < right