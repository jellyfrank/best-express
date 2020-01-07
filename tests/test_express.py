#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from best.api import Best


class TestExpress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.best = Best("KDTESTJSON", "12345", sandbox=True)

    def test_get_express_info(self):
        res = self.best.express.get_express_info(["210323413836"])
        print(res)

if __name__ == "__main__":
    unittest.main()
