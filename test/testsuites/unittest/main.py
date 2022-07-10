#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:34 PM
# @Author  : Yongchin

import unittest
import os
import sys
from test.testsuites.unittest.test_success import UnitTestCase

if __name__ == '__main__':
    # args = ['./testsuites', '-s', '-q', '--report', 'result/report.html']
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # suite.addTest(UnitTestCase("test_case1"))
    suite.addTest(loader.loadTestsFromTestCase(UnitTestCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)