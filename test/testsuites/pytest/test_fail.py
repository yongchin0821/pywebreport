#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 10:12 AM
# @Author  : Yongchin
import pytest


@pytest.fixture()
def user():
    a = "yoyo"
    assert a == "yoyo123"  # fixture failed with error
    return a


class TestC:
    def test_case1(self):
        f"""test fail"""
        assert 0

    def test_case2(self):
        f"""こんにちは世界"""
        raise IOError(123)

    def test_case3(self, user):
        """test error"""
        assert user == "yoyo"
