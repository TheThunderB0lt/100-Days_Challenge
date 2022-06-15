# Minimize the maximum difference between the heights
# Given heights of n towers and a value k. We need to either increase or decrease the height of every tower by k (only once) where k > 0. 
# The task is to minimize the difference between the heights of the longest and the shortest tower after modifications and output this difference.

def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n-1] - arr[0]

    tempMin = arr[0]
    tempMax = arr[n-1]

    for i in range(1, n):
        tempMin = min(arr[0] + k, arr[i] - k)
        tempMax = max(arr[i-1] + k, arr[n-1] - k)

        ans = min(ans, tempMax - tempMin)
    return ans

##Driver Code
k = 6
n = 6
arr = [1, 10, 14, 14, 14, 15]
ans = getMinDiff(arr, n, k)
print("Maximum Difference is: ", ans)

# Output
# Maximum Difference is:  5

# Time Complexity: O(nlogn)
# Auxiliary Space: O(n)