# coding:utf-8
import requests
import util
import unittest
import time
import json

class AddEvent(unittest.TestCase):

    # 利用time库，生成一个唯一的数字
    num = util.create_num()

    """新增会议接口"""   
    url = 'http://139.199.132.220:9000/event/api/add_event/'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'}
    data = {
        'title': '慧测接口测试'+ num,
        'time': '2018-09-01 15:00:00',
        'address': '汤立路220号1号楼007',
    }
    sign = util.create_sign('75ff30521dd7bafb48e07cf7e0a0b564dd8896a4', data)
    data['sign'] = sign
    event_id = None


    def test_add_event01(self):
        """新增会议-正向流程"""

        res = requests.post(url=self.url, headers=self.headers, data=self.data)
        # 将新增的会议id 赋值给event_id
        self.event_id = json.loads(res.text)['data']['event_id']
        # print(res.text)
        # print(self.event_id)

        # 断言 相应状态码、错误码、以及相应时间
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('error_code'), 0)
        self.assertLess(int(round(res.elapsed.total_seconds()*1000)), 500)
