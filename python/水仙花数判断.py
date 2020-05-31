# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 14:00
# @Author  : 闰土
# @FileName: shuixianhua.py
# @Software: PyCharm
while True:
    num = input('请输入想要判断的数：')
    if(len(num) == 3):
        num = int(num)
        a = num // 100
        b = (num-a*100) // 10
        c = (num-a*100-b*10)
        print('{},{},{}'.format(a,b,c))
        if (a**3 + b**3 +c**3) == num :
            print('这个数是水仙花数，因为{}³+{}³+{}³={}'.format(a,b,c,num))
        else:
            print('这个数不是水仙花数,因为{}³+{}³+{}³={},并不等于{}'.format(a,b,c,a**3 + b**3 +c**3,num))
    else:
        print('请输入三位数')
