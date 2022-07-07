# 2. Even or Odd

# Method 1 : Using Brute Force

num = int(input("Enet the number: "))
if num%2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# Method 2 : Using Ternary Operator

num = int(input("Enter the number: "))
print("Even" if num %2 == 0 else "Odd")