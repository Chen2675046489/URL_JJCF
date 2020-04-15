#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'chengzhi'


from tqsdk import TqApi
import requests
import jsonpath
import time
# 可以指定debug选项将调试信息写入指定的文件中

api = TqApi()
quote = api.get_quote("SHFE.sn2007")
while True:
    # 调用 wait_update 等待业务信息发生变化，例如: 行情发生变化, 委托单状态变化, 发生成交等等
    # 注意：其他合约的行情的更新也会触发业务信息变化，因此下面使用 is_changing 判断 cu2003 的行情是否有变化
    api.wait_update()
    # 只有当 cu2003 的最新价有变化，is_changing才会返回 True
    if api.is_changing(quote, "last_price"):
        last_Price = quote.last_price

        body = {"futureCode": "sn2007"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        time.sleep(0.5)
        res = requests.post(url="http://192.168.10.242:8082/futures/average/queryNewSharingData",
                            json=body, headers=headers, timeout=10)
        formula = "$.model.data[-1:].trade"
        trade = jsonpath.jsonpath(res.json(), formula)[0]
        print("我们的当前价格{}".format(trade))
        print("对方的最新价格{}".format(last_Price))
        if last_Price == trade:
            print("数据匹配通过")
        else:
            print("数据匹配不对，请注意！")

