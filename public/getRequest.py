# coding=utf-8

import json
import requests
import parameter


def getRequest(url, param):
    # 拼接请求地址
    r_url = url + '?' + parameter.getParam(param)
    # print r_url
    # 调用requests库的get()方法,发送请求
    request = requests.get(r_url)
    # 获取返回值
    response = request.text
    # 将返回值转化为python可识别的dict对象
    json_response = json.loads(response)
    return json_response
