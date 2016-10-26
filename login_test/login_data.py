# -*- coding: utf-8 -*-


import xlrd
import os


def get_data(filename='teachers.xlsx'):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    phone = table.col_values(2)
    pw = table.col_values(3)
    cellphone = []
    pwlist = []
    for i in range(1, nrows):
        cellphone.append(int(phone[i]))
        pwlist.append(pw[i])
        print('%s : %s' % (i, cellphone[i-1]))
    print(len(cellphone))
    return cellphone, pwlist


if __name__ == '__main__':
    get_data()