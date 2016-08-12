# coding=utf-8

import json
import unittest
import interfaceAutomationTest.public.getRequest
import interfaceAutomationTest.public.doMysql
import interfaceAutomationTest.public.Order
import time
import interfaceAutomationTest.public.kafkaSend

class OrderDetail(unittest.TestCase):
    def setUp(self):
        self.url = 'http://xxx/third/order/detail'

    def test_getDetail_initOrder(self):
        u"""刚下单-获取订单详情"""
        # orderId = thirdOrder.public.doMysql.data_select(0)
        orderId = interfaceAutomationTest.public.Order.creteOrder()
        param = {'orderId': orderId}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 0)
        self.assertEqual(rs.get('data')['maintainOrder']['status'], 0)

    def test_getDetail_canceled(self):
        u"""已取消-获取订单详情"""
        order = interfaceAutomationTest.public.Order.creteOrder()
        orderId = interfaceAutomationTest.public.Order.orderCancel(order)
        param = {'orderId': orderId}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 0)
        self.assertEqual(rs.get('data')['maintainOrder']['status'], 5)

    def test_getDetail_accept(self):
        u"""400已派单-获取订单详情"""
        orderId = interfaceAutomationTest.public.Order.creteOrder()
        interfaceAutomationTest.public.kafkaSend.accept(orderId)
        time.sleep(5)
        param = {'orderId': orderId}
        rs = interfaceAutomationTest.public.getRequest.getRequest(self.url, param)
        print json.dumps(rs, ensure_ascii=False)
        self.assertEqual(rs.get('code'), 0)
        self.assertEqual(rs.get('data')['maintainOrder']['status'], 0)


if __name__ == '__main__':
    unittest.main()