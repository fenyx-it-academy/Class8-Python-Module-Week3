# Bonus question number 1
y = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
newlist = sorted(y, key=lambda d: d['color'])
print(newlist)


# Bonus question number 1
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x%2 == 0, original_list))
odd_numbers = list(filter(lambda x: x%2 != 0, original_list))
print('original list:',original_list)
print('Even numbers: ', even_numbers)
print('Even numbers: ', odd_numbers)