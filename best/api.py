#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm
from .express import Express

class Best(object):

    def __init__(self,partner_id,partner_key,sandbox=False):
        self.partner_id = partner_id
        self.partner_key = partner_key
        self.sandbox = sandbox

    comm = Comm()
    express = Express()

    