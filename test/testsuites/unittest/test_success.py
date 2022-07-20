#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin
import sys
import warnings
import unittest


class UnitTestSuccessCase(unittest.TestCase):
    def test_case1(self):
        """test pass"""
        assert 1

    def test_case2(self):
        """test warning"""
        warnings.warn(UserWarning("This is a warning msg"))

    @unittest.skip("demonstrating skipping")
    def test_case3(self):
        """test skip"""
        assert 0

    def test_print(self):
        print("this test has print msg")

    def test_err_print(self):
        sys.stderr.write("this test has print msg")
        raise IOError("IOError")
