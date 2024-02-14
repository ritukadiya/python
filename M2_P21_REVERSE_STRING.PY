#Write a Python function to reverses a string if its length is a multiple of 4.
def rev_str_if_mul_4(input_str):
    if len(input_str) % 4 == 0:
        return input_str[::-1]  # Reverse the string using slicing
    else:
        return input_str

# Test the function
s1 = input("enter a string 1: ")
s2 = input("enter a string 2: ")
print("Original string 1:", s1)
print("Reversed string 1:", rev_str_if_mul_4(s1))
print("Original string 2:", s2)
print("Reversed string 2:", rev_str_if_mul_4(s2))