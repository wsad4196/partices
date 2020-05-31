# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 14:13
# @Author  : 闰土
# @FileName: YangHuitriangle.py
# @Software: PyCharm
'''
    *
   ***
  *****
 *******
*********
'''
while 1:
    num = int(input('请输入您想要构建的数字：'))
    for p in range(1,num):
        for j in range(num-p):
            print(' ',end='')
        for j in range(2*p-1):
            print('*',end='')


        print()





