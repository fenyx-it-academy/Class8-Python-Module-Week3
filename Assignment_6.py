#Assignment 6 

orginal_list_of_integer = [1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
print("Original list of integers : ", "\n", orginal_list_of_integer)
evens = list(filter(lambda X : X % 2 == 0 , orginal_list_of_integer))

print("Even numbers from the said list : ", "\n" , evens )

odds = list(filter(lambda x : x % 2 == 1 , orginal_list_of_integer))

print("Odd numbers from the said list :", "\n " , odds)