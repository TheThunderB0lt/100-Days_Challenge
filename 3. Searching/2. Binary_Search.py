# Binary Search Iterative implementation

# Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[] and return the index of x in the array.
# Consider array is 0 base index.

# Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
# The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). 

def binarySearch(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        # mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1

##Driver Code
arr = [10, 20, 30, 40, 50, 60]
key = int(input("Enter elemnent to search: "))
res = binarySearch(arr, 0, len(arr)-1, key)
if res == -1:
    print("Element not found in the array")
else:
    print("Element found at index: %d" %res)

# Output:
# Enter elemnent to search: 30
# Element found at index 2

# Enter elemnent to search: 70
# Element not found in the array

# Time Complexity: O(log n)
# Auxiliary Space: O(1)