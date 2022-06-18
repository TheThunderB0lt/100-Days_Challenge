# Write a program to calculate pow(x,n)
# Given two integers x and n, write a function to compute xn. We may assume that x and n are small and overflow doesn’t happen.
# Input : x = 2, n = 3
# Output : 8

# Input : x = 7, n = 2
# Output : 49

def power(x, y):
     
    # Return type of pow() function is double
    return int(pow(x, y))
     
# Driver Code
x = int(input("Enter First Number: "))
y = int(input("Enter Power Number: "))
print("The", x,"^",y, "is: ", power(x, y))

# OUTPUT:
# Enter First Number: 3
# Enter Power Number: 4
# The 3 ^ 4 is:  81

# Time Complexity: O(1)
# Auxiliary Space: O(1)