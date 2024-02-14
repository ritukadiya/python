def first_and_last_two_char(str):
    if len(str) < 2:
        return ""  # Return empty string if the length is less than 2
    else:
        return str[:2] + str[-2:]  # Concatenate the first 2 and last 2 characters

s1 = input("enter a string 1: ")
s2 = input("enter a string 2: ")
s3 = input("enter a string 3: ")

print(first_and_last_two_char(s1))  
print(first_and_last_two_char(s2))  
print(first_and_last_two_char(s3))  