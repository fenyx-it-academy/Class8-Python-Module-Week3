def pascal(n):
    out=[1]
    second=[1,1]
    print(out)
    print(second)
    for i in range(3,n+1):
        out=second.copy()
        out.append(1)
        for j in range(i-2):
            out[j+1]=second[j]+second[j+1]
        second=out.copy()
        print(out)

