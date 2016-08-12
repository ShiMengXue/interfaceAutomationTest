# coding=utf-8

import unittest


# ================将用例添加到测试套件===========
def createSuite():
    testSuite = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = r"F:\WorkSpace\automation_test\thirdOrder\testCase"
    # 定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        print test_case
        testSuite.addTests(test_case)
    return testSuite