n = int(input('Line amount of Pascal Triangle to be printed: '))
triangle = [] 
for r in range(n):
    row = [1]*(r+1)
    if r>1:            # exclude first 2 rows from repetetive task below 
        for c in range(1,r):
            row[c] = triangle[r-1][c-1]+triangle[r-1][c]  
    triangle.append(row)    
    print("   ".join( repr(e) for e in triangle[r] ).center(5*n))   