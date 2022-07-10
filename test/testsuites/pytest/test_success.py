#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin
import pytest
import warnings


def test_case1():
    """test pass"""
    assert 1


def test_case2():
    """test warning"""
    warnings.warn(UserWarning("This is a warning msg"))


@pytest.mark.skip()
def test_case3():
    """test skip"""
    assert 0
