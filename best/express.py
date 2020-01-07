#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

# 百世快递接口

from .comm import Comm


class Express(Comm):

    def get_express_info(self, mailnos=[]):
        """
        获取运单信息
        param mailnos: 运单号列表
        """

        data = """{
            "mailNos": {
                "mailNo": mailnos
            }
        }"""
        return self.post(data=data, service_type="KD_TRACE_QUERY")
