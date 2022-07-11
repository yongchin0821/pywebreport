#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:34 PM
# @Author  : Yongchin

import unittest
import os
import sys
from test.testsuites.unittest.test_success import UnitTestCase
from pywebreport import WebReportRunner
import unittestreport

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTest(UnitTestCase("test_case1"))
    # suite.addTest(loader.loadTestsFromTestCase(UnitTestCase))
    suite.addTest(loader.discover("."))
    # suite = loader.loadTestsFromTestCase(UnitTestCase)

    runner = WebReportRunner()
    runner.run(suite)


    # # 1、加载测试用例到套件中
    # suite = unittest.defaultTestLoader.discover('.')
    #
    # # 2、创建一个用例运行程序
    # runner = unittestreport.TestRunner(suite, tester='测试人员—小柠檬',
    #
    #                                    report_dir=".",
    #                                    title='这里设置报告标题',
    #                                    desc='小柠檬项目测试生成的报告描述',
    #                                    templates=3
    #                                    )
    #
    # # 3、运行测试用例
    # runner.run()
