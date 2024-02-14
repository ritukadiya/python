#Write a Python function to insert a string in the middle of a string.
def insert_str_mid(original_str, str_insert):
    mid_index = len(original_str) // 2
    return original_str[:mid_index] + str_insert + original_str[mid_index:]

original_string = input("enter a string: ")
string_to_insert = input("enter a string: ")
result = insert_str_mid(original_string, string_to_insert)
print("Result:", result)
