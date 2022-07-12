#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:34 PM
# @Author  : Yongchin

import unittest
from test.testsuites.unittest.test_success import UnitTestCase
from pywebreport import WebReportRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTest(UnitTestCase("test_case1"))
    # suite.addTest(loader.loadTestsFromTestCase(UnitTestCase))
    # suite = loader.loadTestsFromTestCase(UnitTestCase)
    suite.addTest(loader.discover("."))

    runner = WebReportRunner(report="result/report.html")
    runner.run(suite)
