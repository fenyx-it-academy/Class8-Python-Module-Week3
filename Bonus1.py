"""
Edited from codes I found on the internet.
"""

myList=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]


sorted_list = sorted(myList, key=lambda x: (x['make'], x['model']))

print(sorted_list)
