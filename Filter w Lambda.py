# Python program to filter a list of integers using Lambda
lint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda x: x%2==0
odd = lambda x: x%2==1

print("Even numbers of the list:", list(filter(even,lint)))
print("Odd numbers of the list:", list(filter(odd,lint)))