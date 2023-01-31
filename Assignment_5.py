#Assignment_5 

orginal_list  = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sorted_list = sorted(orginal_list , key = lambda x : x['color'])
print("Orginal list of dictionaries : " , orginal_list)
print("Sorting the list of dictionaries : " , sorted_list)