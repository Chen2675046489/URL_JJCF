#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import re
import json
import jsonpath
from lib.parameter_substitution import parameter_num
from conf.settings import *
from lib.logger import logger
from lib.global_variables import gv
from lib.tqgetdata import get_last_price


def assert_res(assertRes, res):
    res_status = None
    for i in assertRes.split(";"):
        i_ = i.strip("")
        if i_:
            actual_expr = i_.split("=")[0].strip()
            keys = re.findall(PATTERN, actual_expr)
            if keys:
                size = gv.getVar(keys[0])
                actual_expr = parameter_num(actual_expr, size)
                logger.logger.debug("当前获得的期货代码数据是：{}".format(actual_expr))
            actual = jsonpath.jsonpath(json.loads(res), actual_expr)[0]
            expect = i_.split("=")[1].split("|")
            for j in expect:
                parameter = re.findall(PATTERN, j)
                if parameter:
                    code = str(gv.getVar("exg")+'.'+gv.getVar("code"))
                    get_last_price(code)
                    value = gv.getVar(parameter[0])
                    if actual == value:
                        res_status = "pass"
                    elif actual != value:
                        res_status = "fail"
                elif str(actual) == j:
                    res_status = "pass"
                    break
                elif str(actual) != str(j):
                    res_status = 'fail'
    return res_status
