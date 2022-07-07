# 4. Greatest of 3 numbers

# Input : 20 30 10
# Output : 30

# Method 1: Using if-else Statements
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

if a >= b and a >= c:
    print(a, "is Greater")
elif b >= a and b >= c:
    print(b, "is Greater")
else:
    print(c, "is Greater")


# Method 2: Using Ternary Operator
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

max = a if a >= b else b
max = c if c >= max else max

print(max, "is Greater")