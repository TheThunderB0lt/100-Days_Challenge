# 9. Palindrome checking

# Input : 1221
# Output : Palindrome

# Method 1: Using String Slicing
inp = input("Enter the Input: ")
rev = str(inp[::-1])

if inp == rev:
    print(inp, "is Palindrome")
else:
    print(inp, "is not a Palindrome")
