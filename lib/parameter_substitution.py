#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记


from conf.settings import PATTERN
from lib.global_variables import gv
import random
import re


def parameter_substitution(strParam):
    """依赖参数值替换为实际值"""
    keys = re.findall(PATTERN, strParam)
    for key in keys:
        value = gv.getVar(key)
        strParam = strParam.replace('${' + key + '}', str(value))  # replace返回替换后的新字符串
    return strParam


def parameter_num(numParam, size):
    keys = re.findall(PATTERN, numParam)
    for key in keys:
        num = random.randint(0, size)
        numParam = numParam.replace('${' + key + '}', str(num))
    return numParam


if __name__ == '__main__':
    # strParam = parameter_substitution("${token}")
    # print(strParam)
    numParam = parameter_num("$.model[${id}].exg")
    print(numParam)
