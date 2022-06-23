# # Pascal’s Triangle

# Pascal’s Triangle -> ( O(n^2) time and O(1) extra space ) 
# This method is based on method 1. We know that ith entry in a line number line is Binomial Coefficient C(line, i) and all lines start with value 1. The idea is to calculate C(line, i) using C(line, i-1). It can be calculated in O(1) time using the following. 

## Approach
# C(line, i)   = line! / ( (line-i)! * i! )
# C(line, i-1) = line! / ( (line - i + 1)! * (i-1)! )
# We can derive following expression from above two expressions.
# C(line, i) = C(line, i-1) * (line - i + 1) / i

# So C(line, i) can be calculated from C(line, i-1) in O(1) time


def pascalTriangle(num):
    for line in range(1, num + 1):
        C = 1
        for i in range(1, line +  1):
            print(C, end=" ")
            C = int(C * (line - i) / i)
        print(" ")

## Driver Code
num = int(input("Enter the number of lines: "))
pascalTriangle(num)

# OUTPUT:
# Enter the number: 6
# 1
# 1 1
# 1 2 1
# 1 3 3 1        
# 1 4 6 4 1      
# 1 5 10 10 5 1 
