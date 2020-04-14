#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'chengzhi'
from lib.global_variables import gv
from tqsdk import TqApi


def get_last_price(code):
    # 创建API实例.
    api = TqApi()
    # 获得上期所 cu2003 的行情引用，当行情有变化时 quote 中的字段会对应更新
    quote = api.get_quote(code)
    # 输出 cu2003 的最新行情时间和最新价
    last_price = quote.last_price
    # 关闭api,释放资源
    api.close()

    gv.setVar("last_price", last_price)
    print(last_price)


if __name__ == '__main__':
    get_last_price("CZCE.AP005")
