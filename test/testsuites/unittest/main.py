#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:34 PM
# @Author  : Yongchin
import sys
import unittest
from test_success import UnitTestSuccessCase
from pywebreport import WebReportRunner
from XTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTest(UnitTestSuccessCase("test_case1"))
    # suite.addTest(UnitTestSuccessCase("test_case2"))
    # suite.addTest(loader.loadTestsFromTestCase(UnitTestCase))
    # suite = loader.loadTestsFromTestCase(UnitTestCase)
    suite.addTest(loader.discover("."))

    runner = WebReportRunner(report="result/index.html")
    test_result = runner.run(suite)
