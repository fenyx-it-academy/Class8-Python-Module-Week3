#Python program to sort a list of dictionaries using Lambda
ldict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
a = sorted(ldict, key=lambda x:x['color'])
print(f"\n {a} \n")