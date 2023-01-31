orginal_list  = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sorted_list=sorted(orginal_list, key=lambda x:x["color"])


print(sorted_list)