#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 2:38 PM
# @Author  : Yongchin
import ddt
import unittest


@ddt.ddt
class UnitTestDDT(unittest.TestCase):
    Testdata = [
        ("1+2", 2),
        ("3+5", 8)
    ]

    @ddt.data(*Testdata)
    def test_case1(self, Testdata):
        """ddt case"""
        assert eval(Testdata[0]) == Testdata[1]
