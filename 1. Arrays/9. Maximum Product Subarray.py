# Maximum Product Subarray

# Given an array that contains both positive and negative integers, find the product of the maximum product subarray. Expected Time complexity is O(n) and only O(1) extra space can be used.

def maxSubArrayProduct(arr, n):
    
    max_P = arr[0]
    min_P = arr[0]
    max_so_far = arr[0]

    for i in range(1, n):

        temp = max(max(arr[i], arr[i]*max_P), arr[i]*min_P)
        min_P = min(min(arr[i], arr[i]*min_P), arr[i]*min_P)
        max_p = temp
        max_so_far = max(max_so_far, max_p)

    return max_so_far

##Driver code
arr = [6, -3, -10, 0, 2]
n = len(arr)
print("Maximum Sub array product is:", maxSubArrayProduct(arr, n))

# Output
# Maximum Sub array product is: 180


# Maximum Product Subarray
# Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

class Solution:
    def maxSubArrayProduct(arr, n):

        cur_P = 1
        max_P = -float('inf')
            
        for i in range(n):
            cur_P = cur_P * arr[i]
            if cur_P == 0:
                cur_P = 1
            max_P = max(max_P, cur_P)
            
        cur_P = 1
        res = -float('inf')
        for i in range(n-1, -1, -1):
            cur_P = cur_P * arr[i]
                
            if cur_P == 0:
                cur_P = 1
            res = max(res, cur_P)
            
        return max(res, max_P)

##Driver code
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1