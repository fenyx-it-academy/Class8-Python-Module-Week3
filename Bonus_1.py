dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max',
        'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print('Sorting the List of dictionaries based on make:',sorted(dict, key=lambda i: i['make']))
print('Sorting the List of dictionaries based on color:',sorted(dict, key=lambda i: i['color']))