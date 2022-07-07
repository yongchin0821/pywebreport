#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin
import pytest
import warnings


def test_case1():
    """成功的用例"""
    assert 1


def test_case2():
    """警告的用例"""
    warnings.warn(UserWarning("api v1, should use functions from v2"))


@pytest.mark.skip()
def test_case3():
    """跳过的用例"""
    assert 0
