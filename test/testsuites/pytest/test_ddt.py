#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 2:38 PM
# @Author  : Yongchin
import pytest


class Testddt:
    @pytest.mark.parametrize(
        "test_input,expected", [
            ("1+2", 2),
            ("3+5", 8)
        ]
    )
    def test_case1(self, test_input, expected):
        """ddt case"""
        assert eval(test_input) == expected
