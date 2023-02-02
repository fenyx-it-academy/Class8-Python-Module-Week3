def shift_list(list_, a):
    if a >= 0:
        return list_[-a:] + list_[:-a]
    else:
        a = abs(a)
        return list_[a:] + list_[:a]

#Check the function 
check_func = ['a', 'b', 'c', 'd', 'e', 'f']
print(shift_list(check_func, 4)) 
print(shift_list(check_func, -4))
