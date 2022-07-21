#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin


import unittest


class UnitTestFailCase(unittest.TestCase):
    def test_case1(self):
        """test fail"""
        assert 0

    def test_case2(self):
        """こんにちは世界"""
        raise IOError(123)

    def user(self):
        a = "yoyo"
        assert a == "yoyo123"  # fixture failed with error
        return a

    def test_case3(user):
        """test error"""
        assert user == "yoyo"
