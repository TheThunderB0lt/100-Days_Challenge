# Quick Sort
# In this algorithm, we partition the list around a pivot element, sorting values around the pivot. 
# In my solution, I used the last element from the list as a pivot value. 
# Best performance is achieved when the pivot value splits the list into two almost equal halves.

def quickSort(arr, left, right):
    if left < right: # The subarraay contains atleast 2 elements

        partition_pos = partition(arr, left, right)
        quickSort(arr, left, partition_pos - 1) # index left to partition-1 ie; greater than pivot element
        quickSort(arr, partition_pos + 1, right)  #index right to partition+1 ie; smaller than pivot element
    
# partition function
def partition(arr, left, right):
    i = left #left element
    j = right - 1 #right element
    pivot = arr[right] #last element in the array

    while i < j:
        while i < right and arr[i] < pivot: #moving elements to right
            i += 1
        
        while j > left and arr[j] >= pivot: #moving elements to left
            j -= 1

        if i < j: #Swapping the elements to left & right
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot: # Swapping ivot element to the position
        arr[i], arr[right] = arr[right], arr[i]

    return i #returning the outpu index

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

##Driver Code
if __name__ == '__main__':
    arr = [2,6,5,1,7,4,3]
    print("Given array is: ", end=" ")
    printList(arr)
    quickSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", end=" ")
    printList(arr)     

# Output:
# Given array is:  2 6 5 1 7 4 3 
# Sorted array is:  1 2 3 4 5 6 7 

# Recursive
# In place
# Unstable
# O(nlogn)