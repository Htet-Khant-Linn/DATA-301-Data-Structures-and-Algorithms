# def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s

# print(reverse_string("Hello"))

def reverse_string(s):
    if s == "":
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("Hello"))

