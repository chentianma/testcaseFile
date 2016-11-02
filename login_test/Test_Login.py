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
        try:
            data = xlrd.open_workbook(filename)
            self.table = data.sheets()[0]
            self.nrows = self.table.nrows
            self.ncols = self.table.ncols
            self.phone = self.table.col_values(2)
            self.pw = self.table.col_values(3)
            self.cellphone = []
            self.pwlist = []
        except Exception as err:
            print(err)

        for i in range(1, self.nrows):
            self.cellphone.append(int(self.phone[i]))
            self.pwlist.append(int(self.pw[i]))
            # print('%s : %s' % (i, cellphone[i - 1]))
        return self.cellphone, self.pwlist

    def test_login(self):
        celllist, pwlist = self.get_data()
        n = len(celllist)
        error = 0
        list = []
        for i in range(0, n):
            userid = celllist[i]
            password = pwlist[i]
            data = {'loginId': userid,
                    'loginType': 'phone',
                    'loginPassword': password}

            try:
                url = 'http://qudu.joy-read.com/member/login'
                r = requests.get(url, params=data)
                re_json = json.loads(r.text)
            except Exception as e:
                logging.warning('Bad request!')

            if r.status_code == requests.codes.ok:
                if re_json['resultStatus']:
                    logging.info(':User login successfully!')
                else:
                    error += 1
                    list.append(i)
                    logging.warning(':Login false! ErrorMsg: %s. Current user: %s'
                                % (re_json['errorMsg'], userid))

        time.sleep(3)
        if error >= 1:
            print('ErrorCount : %s' % error)
            print('The list of error: %s' % list)
        elif error == 0:
            print('All users authenticated successfully!')


if __name__ == '__main__':
    unittest.main()
