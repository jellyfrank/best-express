#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from best.api import Best
import json


class TestComm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.best = Best("KDTESTJSON", "12345", sandbox=True)

    def test_sign(self):
        data = """{
    "mailNos": {
        "mailNo": [
            "210323413836"
        ]
    }
}"""
        res = self.best.comm.sign(data)
        self.assertEqual(res, "d4b5fb49d0de80a837a34d8e8c315724", res)


if __name__ == "__main__":
    unittest.main()
