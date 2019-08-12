import math
class Point:
    def __int__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
class Getlen:
    def __init__(self,p1,p2):
        self.x=p1.getx()-p2.getx()
        self.y=p1.gety()-p2.gety()
        self.len=math.sqrt((self.x**2)+(self.y**2))
    def getlen(self):
        return self.len
p1=Point(1,1)
p2=Point(1,2)
l=Getlen(p1,p2)
d=l.getlen()    

