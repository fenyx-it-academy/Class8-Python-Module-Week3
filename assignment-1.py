

def get_pascal(n):

    for x in range(n+1):
        print ("")

        z = 1
        for y in range(1, x+1):
            #print(C, ' ', sep='', end='')
            print (z , end=" ")
            z = z * (x - y) 
            z = z // y
        #print()


result = get_pascal(5)
print (result)


