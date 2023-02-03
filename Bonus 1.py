
list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

new_list = sorted(list, key=lambda x: x['color'])


print(new_list)