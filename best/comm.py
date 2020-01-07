#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

import requests
from hashlib import md5
import urllib.parse
import json

TESTURL = "http://kdtest.800best.com/kd/api/process"
URL = "http://kd.800best.com/kd/api/process"


class Comm(object):

    def __get__(self, instance, type):
        self.partner_id = instance.partner_id
        self.partner_key = instance.partner_key
        self.sandbox = instance.sandbox
        return self

    def get_header(self, biz_data, servie_type):
        """获取header"""
        data = {
            "bizData": biz_data,
            "serviceType": servie_type,
            "partnerID": self.partner_id,
            "sign": self.sign(biz_data)
        }
        return data

    def sign(self, biz_data):
        to_sign = f"{biz_data}{self.partner_key}"
        return md5(to_sign.encode('utf-8')).hexdigest().lower()

    def post(self, data, service_type):
        """请求方法"""
        url = TESTURL if self.sandbox else URL
        data = self.get_header(json.dumps(data), service_type)
        headers = {}
        headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        url = f'{url}?{"&".join(f"{k}={v}" for k,v in data.items())}'
        res = requests.post(url, headers=headers).json()
        return res
