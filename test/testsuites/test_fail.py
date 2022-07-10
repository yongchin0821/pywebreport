#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin
import pytest


def test_case1():
    """test fail"""
    assert 0


def test_case2():
    """こんにちは世界"""
    raise IOError(123)


@pytest.fixture()
def user():
    a = "yoyo"
    assert a == "yoyo123"  # fixture failed with error
    return a


def test_case3(user):
    """test error"""
    assert user == "yoyo"
