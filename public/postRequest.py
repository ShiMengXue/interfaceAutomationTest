# coding=utf-8

import json
import requests
import parameter


def postRequest(url, param):
    # 传入接口地址及参数，发送post请求
    request = requests.post(url, parameter.postData(param))
    # 获取返回值
    response = request.text
    # 将返回值转化为python可识别的dict对象
    json_response = json.loads(response)
    return json_response