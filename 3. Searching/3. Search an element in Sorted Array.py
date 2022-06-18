# Search an element in Sorted Array
# Search Operation
# In a sorted array, the search operation can be performed by using binary search.


def SearchSortedElement(arr, low, high, key):

    mid = low + (high - low) // 2  # dividing into half

    if (key == arr[int(mid)]): #If key found return index
        return mid
    
    if (key > arr[int(mid)]): #If key if greater than middle ele it search to right
        return SearchSortedElement(arr, mid+1, high, key)
    
    if (key < arr[int(mid)]): #If key if smaller than middle ele it search to left
        return SearchSortedElement(arr, low, mid-1, key)

    return 0 #If element not found then it return 0

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
print("The default array is: ", arr)
key = int(input("Enter element to search: "))
print("Element found at index: ", int(SearchSortedElement(arr, 0, n-1, key)))


# OUTPUT:
# The default array is:  [1,2,3,4,5,6,7,8,9,10]
# Enter element to search: 8
# Element found at index:  7

# Time Complexity of Search Operation: O(Log n) [Using Binary Search] 
# Auxiliary Space: O(logn) due to recursive calls