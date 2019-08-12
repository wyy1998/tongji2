def numberOfDayInYear():
    a=31+28+31+30+31+30+31+31+30+31+30+31
    for year in range(2010,2021,1): 
        i=year
        if year % 4 == 0 and  year % 100 != 0 or year % 400 == 0:
            print('%d年有%d天'%(i,a+1)) 
        else:
            print ('%d年有%d天'%(i,a))  
numberOfDayInYear()
                
                   
                
        
        
                

              
        
