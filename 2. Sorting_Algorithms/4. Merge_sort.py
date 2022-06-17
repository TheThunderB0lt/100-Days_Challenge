# Merge Sort using divide & conquer algorithm

# This is a divide and conquer algorithm. In this algorithm, we split a list in half and keep splitting 
# the list by 2 until it only has a single element. Then we merge the sorted list. We keep doing this until 
# we get a sorted list with all the elements of the unsorted input list.

def mergeSort(arr):

    if len(arr) > 1:

        ## Dividing the array elements
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        mergeSort(left_arr) # Sorting the first half
        mergeSort(right_arr) # Sorting the second half

        ## Comparing the elements
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index

        while i < len(left_arr) and j < len(right_arr):

            ## Checking if left array is greater than right array
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        ##Transferring merged array into left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        ##Transferring merged array into right
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

##Driver Code
if __name__ == '__main__':
    arr = [2,6,5,1,7,4,3]
    print("Given array is: ", end=" ")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end=" ")
    printList(arr)

# Output:
# Given array is:  2 6 5 1 7 4 3 
# Sorted array is:  1 2 3 4 5 6 7 


# Time Complexity: O(n logn),  Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
# T(n) = 2T(n/2) + θ(n)

# The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of Master Method and the solution of the recurrence is θ(nLogn). Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
# Auxiliary Space: O(n)

# Space Complexity :

# • In merge sort all elements are copied into an auxiliary array 
# • so N auxiliary space is required for merge sort.
 

# Algorithmic Paradigm: Divide and Conquer

# Is Merge sort In Place?
#  No in a typical implementation

# Is Merge sort Stable: 
# Yes, merge sort is stable. 
