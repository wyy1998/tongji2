class LinearEquation(object):
    def __init__(self,a,b,c,d,e,f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f
    def getX(self):
        x=(self._e*self._d-self._b*self._f)-(self._a*self._d-self._b*self._c)
        print("x的值：%d"%x)
    def getY(self):
        y=(self._a*self._f-self._e*self._c)-(self._a*self._d-self._b*self._c)
        print("y的值:%d"%y)
    def isSolvable(self):
        if (self._a*self._b)-(self._b*self._c)!=0:
            print("true")
        else:
            print("这个方程无解")
test=LinearEquation(1,2,3,4,5,6)
test.getX()
test.getY()
test.isSolvable()