#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import unittest
from lib.global_variables import gv
from lib.parameter_substitution import parameter_substitution
from ddt import *
import requests
from lib.read_excel import read_excel
from lib.assert_res import assert_res
from conf.settings import SHEET_NAME
from lib.logger import logger
from lib.write_excel import Write
from conf.settings import Result


@ddt
class MyRequest(unittest.TestCase):
    test_datas = read_excel(SHEET_NAME)
    @data(*test_datas)
    @unpack
    def test_my_request_(self, project, case_num, case_id, case_name, description, url, method, headers, params, body, file, init_sql, globalVariable, assertRes, actualResults, result):
        """请求"""
        logger.logger.debug("==========【当前执行用例是：%s：%s】==========" % (case_id, case_name))
        url = parameter_substitution(url)
        headers = parameter_substitution(headers)
        params = parameter_substitution(params)
        body = parameter_substitution(body)
        logger.logger.debug("> > > > >请求的method是：%s" % method)
        logger.logger.debug("> > > > >请求的url是：%s" % url)
        logger.logger.debug("> > > > >请求的headers是：%s" % headers)
        logger.logger.debug("> > > > >请求的params是：%s" % params)
        logger.logger.debug("> > > > >请求的body是：%s" % body)
        logger.logger.debug("> > > > >断言内容assertRes是：%s" % assertRes)

        # 转换
        headers_ = eval(headers) if headers else headers
        params_ = eval(params) if params else params
        body_ = eval(body) if body else body

        if init_sql:
            pass

        # get请参考post完善
        if method.upper() == 'GET':
            try:
                res = requests.get(url=url, headers=headers_, params=params_, timeout=10)
                logger.logger.debug("执行请求后，结果是：%s" % res.text)
                # 如果有需要被后续请求用的变量数据
                if globalVariable:
                    gv.save_global_variable(globalVariable, res.text)

                # 断言
                if assertRes:
                    res_status = assert_res(assertRes, res.text)
                    logger.logger.debug("断言结果是：%s\n\n" % res_status)
                    if res_status == "pass":
                        Write(row=int(case_num), col=Result, value="pass")
                    elif res_status != "pass":
                        Write(row=int(case_num), value=res.text)
                    gv.res.append([res.text, url, headers, body, res_status])
                    self.assertEqual(res_status, "pass")

            except Exception as e:
                print('出错了，错误是%s' % e)
                raise e

        elif method.upper() == 'POST':
            # 执行请求
            try:
                res = requests.post(url=url, headers=headers_, json=body_, timeout=10)
                logger.logger.debug("执行请求后，结果是：%s" % res.text)
                # 如果有需要被后续请求用的变量数据
                if globalVariable:
                    gv.save_global_variable(globalVariable, res.text)

                # 断言
                if assertRes:
                    res_status = assert_res(assertRes, res.text)
                    logger.logger.debug("断言结果是：%s\n\n" % res_status)
                    if res_status == "pass":
                        Write(row=int(case_num), col=Result, value="pass")
                    elif res_status == "fail":
                        Write(row=int(case_num), value=res.text)
                    elif res_status == "nodata":
                        Write(row=int(case_num), value="当前显示没有数据，请注意！{}".format(res.text))
                    gv.res.append([res.text, url, headers, params, body, res_status])
                    self.assertEqual(res_status, "pass")

            except Exception as e:
                print('出错了，错误是%s' % e)
                raise e


if __name__ == '__main__':
    pass
