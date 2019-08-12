class RegularPolygon(object):
    def __init__(self,n,side,x,y):
        self._n = n
        self._side = side
        self._x = x
        self._y = y
    def getPerimeter(self):
        print("多边形周长：%f"%(self._n*self._side))
re = RegularPolygon(6,4,0,0)
re.getPerimeter()