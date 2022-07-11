#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin
import pytest
import warnings


class TestA:
    def test_case1(self):
        """test pass"""
        assert 1

    def test_case2(self):
        """test warning"""
        warnings.warn(UserWarning("This is a warning msg"))


class TestB:
    @pytest.mark.skip()
    def test_case3(self):
        """test skip"""
        assert 0
