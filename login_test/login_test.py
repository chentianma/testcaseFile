# -*- coding: utf-8 -*-


import unittest
import xlrd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def tearDown(self):
        driver = self.driver
        driver.close()

    def get_data(self, filename='teachers.xlsx'):
        data = xlrd.open_workbook(filename)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        print(nrows, ncols)
        phone = table.col_values(2)
        pw = table.col_values(3)
        cellphone = []
        pwlist = []
        for i in range(1, nrows):
            cellphone.append(int(phone[i]))
            pwlist.append(int(pw[i]))
            print('%s : %s' % (i, cellphone[i - 1]))
        return cellphone, pwlist

    def test_login(self):
        filename = None
        celllist, pwlist = self.get_data()
        n = len(celllist)
        driver = self.driver
        driver.get('http://qudu.joy-read.com/read/loginPage')
        # time.sleep(3)
        driver.implicitly_wait(20)
        for i in range(0, n):
            if self.assertIn('趣读-登录页面', driver.title):
                print('登录界面加载成功......')
            cellphone = celllist[i]
            pw = pwlist[i]
            driver.find_element_by_id('loginId').send_keys(cellphone)
            driver.find_element_by_id('loginPassword').send_keys(pw)
            driver.find_element_by_id('loginBtn').click()
            # if self.assertIn('阅读平台', driver.title):
            # logout = driver.find_element_by_link_text('退出账号')
            # logout.click()
            time.sleep(5)
            driver.get('http://qudu.joy-read.com/read/loginPage')

if __name__ == '__main__':
    unittest.main()

