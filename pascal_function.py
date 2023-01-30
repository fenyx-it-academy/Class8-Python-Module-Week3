def pascal_triangle(number):
    row =[1]
    for i in range(number):
        for j in range(i+1):
          print(row[j], end="  ")
        row = [x+y for x, y in zip([0] + row , row + [0])]
        print('\n')
if __name__ == "__pascal_triangle__":
    pascal_triangle()

# .... the program below I wrote at first, which works perfectly but not efficient...........
# def pascal_triangle(number):
#     for i in range (number):
#      pascal_number = i
#      for index in range(i+1):
#         if index == 0:
#             print(index + 1, end="  ")
#         elif index == 1:
#             print(i, end="  ")
#         else:
#             pascal_number *= (i-(index-1))/(index)
#             print (int(pascal_number), end="  " )
#      print('\n')


# pascal sequence: 1 , n , n(n−1)/2 , n(n−1)(n−2)/ 2*3 , n(n−1)(n−2)(n−3)/2*3*4......
