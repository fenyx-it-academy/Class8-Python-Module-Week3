lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
lst.sort(key=lambda x: x ['color'])
print(lst)
