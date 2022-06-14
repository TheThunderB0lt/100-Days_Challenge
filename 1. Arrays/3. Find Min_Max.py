# Find minimum and maximum element in an array
# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function getMinMax() which takes the array A[] and its size N as inputs and returns the minimum and maximum element of the array.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

def getMinMax(arr, n):
    mn = arr[0]
    mx = arr[0]
    for i in arr:
        if i > mx:
            i = mx
        if i > mn:
            i = mn
    return mn, mx

def main():
    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])
        T -= 1

if __name__ == "__main__":
    main()

#  Driver Code Ends

# Input:
# N = 6
# A[] = {3, 2, 1, 56, 10000, 167}
# Output:
# min = 1, max =  10000