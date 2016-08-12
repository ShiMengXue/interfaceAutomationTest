# coding=utf-8

import unittest
import json
import interfaceAutomationTest.public.getRequest


class QueryCity(unittest.TestCase):
    def setUp(self):
        self.url = 'http://xxx/third/order/queryCity'

    def test_get_ok(self):
        u"""成功获取城市"""
        param = {'channel': '10', 'code': '2'}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('data')['name'], u'成都')

    def test_get_fail(self):
        u"""未获取到城市"""
        param = {'channel': '10', 'code': 'error'}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('data'), None)


if __name__ == '__main__':
    unittest.main()
