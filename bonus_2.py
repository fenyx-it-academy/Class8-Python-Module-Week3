integers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_integers=list(filter(lambda x:(x%2==0),integers ))
odd_integers=list(filter(lambda x:(x%2==1),integers ))
print(even_integers)
print(odd_integers)