# -*- coding: utf-8 -*-


import unittest
import requests
import logging
import json
import xlrd
import time


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
)


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def get_data(self, filename='teachers.xlsx'):
        self.file = input('Input the filename:')
        if self.file:
            self.filename = self.file
        else:
            self.filename = filename
        try:
            data = xlrd.open_workbook(self.filename)
            self.table = data.sheets()[0]
            nrows = self.table.nrows
            ncols = self.table.ncols
            self.phone = self.table.col_values(2)
            self.pw = self.table.col_values(3)
            self.cellphone = []
            self.pwlist = []
        except Exception as err:
            print(err)

        for i in range(1, nrows):
            self.cellphone.append(int(self.phone[i]))
            self.pwlist.append(int(self.pw[i]))
            # print('%s : %s' % (i, cellphone[i - 1]))
        return self.cellphone, self.pwlist

    def test_login(self):
        self.celllist, self.pwlist = self.get_data()
        n = len(self.celllist)
        error = 0
        self.list = []

        for i in range(0, n):
            self.userid = self.celllist[i]
            self.password = self.pwlist[i]
            data = {'loginId': self.userid,
                    'loginType': 'phone',
                    'loginPassword': self.password}

            try:
                url = 'http://qudu.joy-read.com/member/login'
                res = requests.get(url, params=data)
                re_json = json.loads(res.text)
            except Exception as e:
                logging.warning('Bad request!')

            if res.status_code == requests.codes.ok:
                if re_json['resultStatus']:
                    logging.info(':User login successfully!')
                else:
                    error += 1
                    list.append(i)
                    logging.warning(':Login false! ErrorMsg: %s. Current user: %s'
                                % (re_json['errorMsg'], self.userid))

        time.sleep(2)
        if error >= 1:
            print('ErrorCount : %s' % error)
            print('The list of error: %s' % self.list)
        elif error == 0:
            print('All users authenticated successfully!')


if __name__ == '__main__':
    unittest.main()
