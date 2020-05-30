# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 12:12
# @Author  : 闰土
# @FileName: PrimeJudgment.py
# @Software: PyCharm

while 1:
    num = int(input('请输入您想要判断的数：'))
    sum = 0
    for p in range(0,num+1):
        for j in range(0,num):
            if p * j == num:
                sum += 1
                print('{}有{}*{}={}'.format(num,p,j,num))

    if sum == 1:
        print('{}是素数'.format(num))
    else:
        print('{}不是素数'.format(num))
