# coding=utf-8

import unittest
import json
import interfaceAutomationTest.public.postRequest
import interfaceAutomationTest.public.doMysql
import datetime


# 定义预约时间生成方法
def produceStartime():
    nowtime = datetime.datetime.now()
    tomorrow = nowtime + datetime.timedelta(days=1)
    startTime = tomorrow.strftime("%Y%m%d%H%M%S")
    return startTime


startTime = produceStartime()  # 生成预约时间


class CreateOrder(unittest.TestCase):
    def setUp(self):
        self.url = 'http://xxx/third/order/create'

    def test_create_ok_full(self):
        u"""订单信息选项全部填写正确，下单成功"""
        param = {'number': 1, 'address': '叶青大厦', 'name': 'Tom','startTime': startTime}
        print self.startTime
        rs = interfaceAutomationTest.public.postRequest.postRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 0)

    def test_create_fail_nocityId(self):
        u"""cityId为空，下单失败"""
        param = {'number': '', 'address': '叶青大厦', 'name': 'Tom', 'startTime': startTime}
        rs = interfaceAutomationTest.public.postRequest.postRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertNotEqual(rs.get('code'), 0, msg=rs.get('code'))


if __name__ == '__main__':
    unittest.main()
