# Move all negative numbers to beginning and positive to end with constant extra space

# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

# Examples : 
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

from doctest import OutputChecker

## Using sort(), it sorts with ascending order
def arrSort(arr):
    arr.sort()

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print("Given Array is: ", arr)
print("After sort:")
arrSort(arr)
for ele in arr:
    print(ele, end=", ")

# Output
# Given Array is:  [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# After sort:
# -13, -12, -7, -6, -5, -3, 5, 6, 11,



## Efficient Approach
# Time complexity: O(N) 
# Auxiliary Space: O(1)

def reArrange(arr, n) :
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    print(arr)

## Driver Code
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
reArrange(arr, n)

# Output
# [-12, -13, -5, -7, -3, -6, 5, 6, 11]