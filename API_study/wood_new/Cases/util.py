#coding:utf-8
import hashlib
import base64
import time
import random


# low
def create_num():
    a = str(time.time())
    # b = a.find('.')  # return 10
    num = a[5:10]
    return num


# high
def create_str(num):
    checkcode = ''
    
    for i in range(num):
        number = random.randint(0, num)
        if i == number:
            tmp = chr(random.randint(65, 90))
        else:
            tmp = random.randint(0, 9)
        checkcode += str(tmp)
    return checkcode


# 对给定的字符串进行base64加密
def base64_encode(source):
    return base64.encodestring(source)


# 根据需求创建sign
def create_sign(token, dic):
    li = []
    for k, v in dic.items():
        if k != 'sign':
            li.append(k+'='+v)

    para = '&'.join(sorted(li))
    str = '%spara=%s' % (token, para)
    md5 = hashlib.md5()
    md5.update(str)
    return md5.hexdigest()

# print(base64_encode('123huicehuice!@#'))

data = {
    'title': '慧测接口测试010',
    'time': '2018-09-01 15:00:00',
    'address': '汤立路220号1号楼007',
}

