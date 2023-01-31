def pascal():

    pascal_list = [[1], [1,1]]

    num = int(input('Enter a number: '))

    for i in range(2, num):
        list1 = [1]
        for j in range (1,i):
            list1.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])

        list1.append(1)
        pascal_list.append(list1)

    triangle = len(pascal_list)
    for i in range(0,triangle):
        print((triangle-i) * " ", pascal_list[i])

pascal()