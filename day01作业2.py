def sumDigits(n):
#str将括号中的内容强制转换为字符串
    str_ = str(n)
    int_ = 0
#Python len() 方法返回对象（str字符、列表、元组等）长度或项目个数
    for i in str_:
        int_ += int(i)
    print(int_)
sumDigits(222)