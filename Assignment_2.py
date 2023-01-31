#Answer 2
# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# Sample Items : green-red-yellow-black-white Expected Result : black-green-red-white-yellow#

items = []
def res(n):
    for i in n:
        items.append(i)
        items.sort()
    return "-".join(items)
user_input = input("Enter:").split("-")
print(res(user_input))
