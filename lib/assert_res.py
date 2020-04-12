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
            if isinstance(actual, list):
                """判断当前的数据列表是否为空"""
                if len(actual) <= int(expect[0]):
                    res_status = "nodata"
                    logger.logger.debug("当前数据返回为空，请注意线上数据")
                    return res_status
                else:
                    res_status = "pass"
                    return res_status
            for j in expect:
                if str(actual) == j:
                    res_status = "pass"
                    break
                elif str(actual) != str(j):
                    res_status = 'fail'
    return res_status
