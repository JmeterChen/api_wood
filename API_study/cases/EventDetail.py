#coding:utf-8
import requests
import util
import unittest

class EventDetail(unittest.TestCase):
    '''获取会议详细信息接口'''
    def test_get_eventdetail01(self):
        '''会议详细信息接口-正向流程'''
        url = 'http://139.199.132.220:9000/event/api/get_eventdetail/'
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'}
        data = {
            'id': '1635'
        }
        sign = util.create_sign('75ff30521dd7bafb48e07cf7e0a0b564dd8896a4', data)
        data['sign'] = sign
        res = requests.get(url=url,
                      headers=headers,
                      params=data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json().get('error_code'), 0)
        self.assertEqual(res.json().get('event_detail').get('id'), '1635')
        self.assertLess(int(round(res.elapsed.total_seconds()*1000)), 500)