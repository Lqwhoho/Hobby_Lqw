#!C:\Users\liuquanwei\AppData\Local\Programs\Python\Python37
# -*- coding:utf-8 -*-
# @Author：liuquanwei
# @Time：2019/10/23 14:37
# @Filename：ID_Card.py
# @Desc：====================================================
"""
根据火车票中的部分身份证号码推断出全部身份证号码
首先根据年份，写出那一年的所有日期，格式为年月日
然后通过id_validator库过滤出有效合法的身份证号码
最后把过滤出来的身份证号码在12306网站添加常用联系人进行验证，直到验证为通过状态
"""
# @Software：PyCharm
import time


# 生成出生当年所有日期


def dateRange(year):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(year+'-01-01', fmt)))
    end = int(time.mktime(time.strptime(year+'-12-31', fmt)))
    list_date = [time.strftime(fmt, time.localtime(i)) for i in range(bgn, end+1, 3600*24)]
    return [i.replace('-', '') for i in list_date]


data_time = dateRange('1993')
print(data_time)
print(len(data_time))


from id_validator import validator

# 遍历所有日期，print通过校验的身份证号码，验证身份证号合法性


def vali_dator(id1, id2, id3):
    for i in dateRange(id2):
        theid = id1 + i + id3
        if validator.is_valid(theid):
            print(theid)


vali_dator('522633', '1995', '6028')
