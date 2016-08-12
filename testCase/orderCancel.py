# coding=utf-8

import json
import unittest
import interfaceAutomationTest.public.doMysql
import interfaceAutomationTest.public.postRequest
import interfaceAutomationTest.public.Order
import interfaceAutomationTest.public.kafkaSend
import time


class OrderCancel(unittest.TestCase):
    def setUp(self):
        self.url = 'http://xxx/third/order/cancel'

    def test_cancel_initOrder(self):
        u"""取消刚提交的订单"""
        # orderId = thirdOrder.public.doMysql.data_select(0)
        orderId = interfaceAutomationTest.public.Order.creteOrder()
        param = {'orderId': orderId}
        rs = interfaceAutomationTest.public.postRequest.postRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        if rs.get('data'):
            interfaceAutomationTest.public.doMysql.data_update(orderId)
        else:
            print '订单取消失败！'

    def test_cancel_canceled(self):
        u"""重复取消订单"""
        # orderId = thirdOrder.public.doMysql.data_select(5)
        order = interfaceAutomationTest.public.Order.creteOrder()
        orderId = interfaceAutomationTest.public.Order.orderCancel(order)
        param = {'orderId': orderId}
        rs = interfaceAutomationTest.public.postRequest.postRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('data'), True)

    def test_cancel_notOrder(self):
        u"""订单号不存在取消失败"""
        orderId = 888888
        param = {'orderId': orderId}
        rs = interfaceAutomationTest.public.postRequest.postRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('data'), False)


if __name__ == '__main__':
    unittest.main()