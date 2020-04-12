#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import os
import time
from datetime import datetime, timedelta

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义测试用例的目录路径
TESTCASE_PATH = os.path.join(BASE_PATH, 'test_case')
# 定义测报告的目录路径
REPORT_PATH = os.path.join(BASE_PATH, 'report/')
# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH, 'log/log.txt')
# 定义测试数据的目录路径
DATA_PATH = os.path.join(BASE_PATH, 'data')
# 定义测试数据文件
FILE_PATH = os.path.join(DATA_PATH, 'testcase.xlsx')
# project env
HOST_INFO = {
	'dev': 'http://127.0.0.1:9999',
	'test': 'http://127.0.0.1:9999',
	'preProduct': 'http://127.0.0.1:9999'
}

# 当前要运行的sheet名
# SHEET_NAME = "lc"
SHEET_NAME = "Sheet1"

# sheet名及索引
SHEET_INFO = {
	'Sheet1': 0
}

# 测试环境
# PROJECT_IP1 = '192.168.10.242:8081'
# PROJECT_IP2 = '192.168.10.242:8082'
# PROJECT_IP3 = '192.168.10.242:8083'
# 生产环境
PROJECT_IP1 = 'app.jiangjuncj.com'
PROJECT_IP2 = 'stock.jiangjuncj.com'
PROJECT_IP3 = 'new.jiangjuncj.com'

# mysql数据库的连接信息
MYSQL_HOST = ''
MYSQL_PORT = 3806
MYSQL_DB_USER = 'root'
MYSQL_DB_PASSWORD = ''
MYSQL_DB_NAME = 'qzcsbj'

# redis数据库的连接信息
# r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='qzcsbj@redis666')
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 'qzcsbj@redis666'

# print(BASE_PATH)
# print(TESTCASE_PATH)
# print(REPORT_PATH)
# print(LOG_PATH)

# 参数替换，获取key
PATTERN = '\$\{(.*?)\}'

# excel表中返回报文的列数
ActualResults = 15
# excel表中测试结果的列数
Result = 16

# 上个星期的日期
yesterday = int(time.mktime(time.strptime(str(datetime.today().date() - timedelta(days=7)), '%Y-%m-%d'))*1000)
# 当前的时间
today = int(datetime.now().timestamp()*1000)
# 上一年的时间
year_time = time.strftime('%Y', time.localtime(time.time()))
month_day = time.strftime('%m-%d', time.localtime(time.time()))
last_year = int(time.mktime(time.strptime('{}-{}'.format(str(int(year_time) - 1), month_day), '%Y-%m-%d'))*1000)

if __name__ == '__main__':
	print(month_day)

