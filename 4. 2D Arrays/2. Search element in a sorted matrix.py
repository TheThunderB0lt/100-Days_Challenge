# # Search element in a sorted matrix

# Given a sorted matrix mat[n][m] and an element ‘x’. Find the position of x in the matrix if it is present, else 
# print -1. Matrix is sorted in a way such that all elements in a row are sorted in increasing order and for row ‘i’, 
# where 1 <= i <= n-1, the first element of row ‘i’ is greater than or equal to the last element of row ‘i-1’. 
# The approach should have O(log n + log m) time complexity.

# A Simple Solution is to one by one compare x with every element of the matrix. If matches, then return position. 
# If we reach the end, return -1. The time complexity of this solution is O(n x m).

# Method 2: Using binary search in 2 dimensions

# This method also has the same time complexity: O(log(m) + log(n)) and auxiliary space: O(1), but the algorithm 
# is much easier and the code way cleaner to understand.

# Approach: We can observe that any number (say k) that we want to find, must exist within a row, including the 
# first and last elements of the row (if it exists at all). So we first find the row in which k must lie 
# using binary search ( O(logn) ) and then use binary search again to search in that row( O(logm) ).


def findRow(arr, row, col, k):
    low = 0
    high = row - 1
    mid = 0

    while(low <= high):
        mid = int((low + high) / 2)

        if (k == arr[mid][0]): #checking leftmost elements
            print("Found at index: (", mid, ",", "0)", sep='')
            return 
        
        if (k == arr[mid][col-1]): #Checking rightmost elements
            t = col - 1
            print("Found at index: (", mid, ",", t, ")", sep='')
            return

        if (k > arr[mid][0] and k < arr[mid][col-1]):
            binarySearch(arr, row, col, k, mid)
            return

        if (k < arr[mid][0]):
            high = mid - 1

        if (k > arr[mid][col-1]):
            low = mid + 1

def binarySearch(arr, row, col, k, x):
    low = 0
    high = col - 1
    mid = 0

    while(low <= high):
        mid = int((low+high)/2)

        if (arr[x][mid] == k):
            print("Found at index: (" , x , ",", mid , ")", sep = "")
            return

        if (arr[x][mid] > k):
            high = mid -1
        
        if (arr[x][mid] < k):
            low = mid + 1

    print("Element not found")

##Driver Code
row = 4
col = 4
arr = [ [1,2,3,4], 
        [5,6,7,8], 
        [9,10,11,12], 
        [13,14,15,16]]
        
print(arr)
k = int(input("Enter element to search its index: "))
findRow(arr, row, col, k)
