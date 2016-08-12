# coding=utf-8
import time
import HTMLTestRunner


def report_info():
    now = time.strftime("%Y-%m-%d%H%M%S")
    report_path = 'F:\\WorkSpace\\automation_test\\thirdOrder\\report\\'
    reportFile = report_path + now + 'result.html'
    testReport = file(reportFile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=testReport,
        title=u'接口测试报告',
        description=u'用例执行情况：')
    return report_path, testReport, runner