## Assignment 1

# Write a Python function that prints out the first n rows of Pascal's triangle.

N=int(input("Insert number of rows in Pascal's triangle "))
P=[]

for i in range (N):
    row = [1]*(i+1) #this is first 1
    for j in range (i+1):
        if j!=0 and j!=i: # if itis not first and last position, then we make a calculation 
            row[j]=P[i-1][j-1] + P[i-1][j] #calculation acording to the formula
    P.append(row) # make a list with nested lists

for r in P:
  print(r) #print every list from new line


