# coding=utf-8


import json
import unittest
import interfaceAutomationTest.public.getRequest
import interfaceAutomationTest.public.doMysql
import datetime

class QueryList(unittest.TestCase):
    def setUp(self):
        self.url = 'http://xxx/third/order/queryList'

    def produceTime(self):
        nowtime = datetime.datetime.now()
        start = nowtime - datetime.timedelta(days=2)
        end = nowtime + datetime.timedelta(days=2)
        self.startDate = start.strftime("%Y%m%d%H%M%S")
        self.endDate = end.strftime("%Y%m%d%H%M%S")

    def test_queryList_ok(self):
        u"""获取某个时间段的历史订单"""
        self.produceTime()
        param = {'startDate': self.startDate,
                 'endDate': self.endDate,
                 'channel': 10,
                 'pageSize': 10,
                 'currentPage': 1}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 0)
        self.assertEqual(rs.get('data')['currentPage'], 1)

    def test_queryList_fail(self):
        u"""不传渠道号，获取失败"""
        self.produceTime()
        param = {'startDate': self.startDate,
                 'endDate': self.endDate,
                 'channel': '',
                 'pageSize': 10,
                 'currentPage': 1}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertNotEqual(rs.get('code'), 0)

if __name__ == '__main__':
    unittest.main()