# coding=utf-8

# Linux
import sys
# sys.path.append("/data/testTools/automation_test/")
import interfaceAutomationTest.public.reportInfo
import interfaceAutomationTest.public.createSuite
import interfaceAutomationTest.public.sendReport
import interfaceAutomationTest.public.doMysql

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    report_path, testReport, runner = interfaceAutomationTest.public.reportInfo.report_info()
    allTestCase = interfaceAutomationTest.public.createSuite.createSuite()
    runner.run(allTestCase)
    testReport.close()  # 关闭生成的报告
    try:
       interfaceAutomationTest.public.sendReport.send_report(report_path)  # 发送报告
    finally:
        interfaceAutomationTest.public.doMysql.update_order_queue()