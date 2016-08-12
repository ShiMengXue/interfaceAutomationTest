# coding=utf-8

from kafka import KafkaClient, SimpleProducer
import orderQuery
import Order
import random
import json


def randoms(x):
    rand = int(random.random()*10000)
    id = x*10000+rand
    return id

id = randoms(3005)

def msgConf(order_state, orderId):
    msgd = {
        'test01': id,
        'test02': id
    }
    msg = json.dumps(msgd)
    return msg

# 已派单
def accept(orderId):
    kafka = KafkaClient("ip", 'port')
    producer = SimpleProducer(kafka)
    producer.send_messages('order_test', msgConf(181, orderId))
