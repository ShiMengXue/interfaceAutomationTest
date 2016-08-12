# coding=utf-8

import unittest
import json
import interfaceAutomationTest.public.getRequest


class QueryCityList(unittest.TestCase):
    def setUp(self):
        self.url = 'http://xxx/third/order/queryCityList'

    def test_get_ok(self):
        u"""获取城市列表成功"""
        param = {'channel': '10'}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 0)

    def test_get_fail(self):
        u"""获取城市列表失败"""
        param = {'channel': 'abc'}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 4010)
if __name__ == '__main__':
    unittest.main()