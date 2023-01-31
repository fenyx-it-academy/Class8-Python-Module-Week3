dictionaries = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# the output shown in the readme file suggests it's sorting by "color" key?
sorted = sorted(dictionaries, key = lambda x:x["color"])


print (sorted)