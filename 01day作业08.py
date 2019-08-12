def numberOfDayInYear():
    a=31+28+31+30+31+30+31+31+30+31+30+31
    for year in range(2010,2021,1): 
            import math
def prime():
    num=[]
    i=2
    for i in range(2,32):
        j=2
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            num.append(i)
    return num
def misen():
    print('p        2^p-1')
    a=prime()
    for p in range(1,32):
        for i in range(11):
            if (2**p)-1==a[i]:
                print("%d         %d" %(p,a[i]))
misen()    
                   
                
        
        
                

              
        
