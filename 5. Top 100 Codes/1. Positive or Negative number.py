# 1. Positive or Negative number:

# Input : num = 20
# Output : The number is Positive.

#  Method 1: Using Brute Force

num = int(input("Enter the number:"))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("Zero")


# Method 2: Using Ternary Operator
# Ternary Operator Syntax
# ( Condition ) ? ( if True : Action) : ( if False : Action) ;

num = int(input("Enter the number:"))
print("Positive" if num >= 0 else "Negative")