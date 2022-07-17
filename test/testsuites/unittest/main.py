#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:34 PM
# @Author  : Yongchin

import unittest
from test_success import UnitTestSuccessCase
from pywebreport import WebReportRunner
from XTestRunner import HTMLTestRunner
if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(UnitTestSuccessCase("test_loguru"))
    # suite.addTest(loader.loadTestsFromTestCase(UnitTestCase))
    # suite = loader.loadTestsFromTestCase(UnitTestCase)
    # suite.addTest(loader.discover("."))

    runner = WebReportRunner(report="result/report.html")
    test_result = runner.run(suite)
    # for case, reason in test_result.failures:
    #     print(case.id())
    #     print(reason)

    # with(open('result/report.html', 'wb')) as fp:
    #     runner = HTMLTestRunner(
    #         stream=fp,
    #         title='test report',
    #         description='describe: ... ',
    #         language='en',
    #     )
    #     runner.run(
    #         testlist=suite,
    #         rerun=2,
    #         save_last_run=False
    #     )