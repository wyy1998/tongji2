def getPentagonalNumber(n):
    c = n*(3*n-1)/2
    if n%10 !=0:
        print(c,end='\t')
    else:
        print(c)
        
for i in range(1,101):
    getPentagonalNumber(i)