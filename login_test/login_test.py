# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.userList = {
            13700000000: '11111',
        }

    def tearDown(self):
        pass

    def test_login(self):
        userList = self.userList
        driver = self.driver
        driver.get('http://qudu.joy-read.com/read/loginPage')
        time.sleep(5)
        # driver.implicity_wait(20)
        for list in userList:
            if self.assertIn('趣读-登录页面', driver.title):
                print('登录界面加载成功......')
            print(list)
            user = list
            passId = list
            # loginid = driver.find_elemnet_by_id('loginId')
            # loginid.send_keys(user)
            # password = driver.find_elemnet_by_id('loginPassword')
            # password.send_keys(passId)
            # submit = driver.find_elemnet_by_id('loginBtn')
            # submit.click()


if __name__ == '__main__':
    unittest.main()

